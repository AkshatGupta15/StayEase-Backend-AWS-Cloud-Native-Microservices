# user_service.py (Lambda handler with robust debug + cleaner handling)
import json
import boto3
import os
import traceback

def _response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

# Load environment variables
print("Loading environment variables...")
try:
    USER_POOL_ID = os.environ["USER_POOL_ID"]
    CLIENT_ID = os.environ["CLIENT_ID"]
    # print(f"USER_POOL_ID: {USER_POOL_ID}")
    # print(f"CLIENT_ID: {CLIENT_ID}")
except Exception as e:
    print("Environment variable error:", str(e))
    raise

# Init Cognito client
client = boto3.client("cognito-idp")


# --- USER HANDLERS ---
def register_user(event):
    print("Inside register_user")
    try:
        body = json.loads(event.get("body", "{}"))
        email = body.get("email")
        password = body.get("password")

        if not email or not password:
            return _response(400, {"error": "Email and password are required."})

        print(f"Registering user: {email}")

        response = client.sign_up(
            ClientId=CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[{"Name": "email", "Value": email}]
        )
        print("Sign up success:", response)
        return _response(201, {"message": "User registered. Please verify your email."})

    except client.exceptions.UsernameExistsException:
        print("User already exists")
        return _response(409, {"error": "User already exists."})
    except Exception as e:
        print("Registration error:", str(e))
        traceback.print_exc()
        return _response(500, {"error": str(e)})


def login_user(event):
    print("Inside login_user")
    try:
        body = json.loads(event.get("body", "{}"))
        email = body.get("email")
        password = body.get("password")

        if not email or not password:
            return _response(400, {"error": "Email and password are required."})

        print(f"Logging in user: {email}")

        response = client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": email, "PASSWORD": password}
        )

        auth_result = response["AuthenticationResult"]
        print("Login successful.")

        return _response(200, {
            "access_token": auth_result["AccessToken"],
            "id_token": auth_result["IdToken"],
            "refresh_token": auth_result.get("RefreshToken")
        })

    except client.exceptions.NotAuthorizedException:
        print("Incorrect credentials")
        return _response(401, {"error": "Incorrect username or password."})
    except client.exceptions.UserNotFoundException:
        print("User not found")
        return _response(404, {"error": "User not found."})
    except Exception as e:
        print("Login error:", str(e))
        traceback.print_exc()
        return _response(500, {"error": str(e)})


# --- Lambda Entrypoint ---
def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    # For payload v2.0
    method = event.get("requestContext", {}).get("http", {}).get("method")
    path = event.get("requestContext", {}).get("http", {}).get("path")
    print(f"Method: {method}, Path: {path}")

    if method == "POST" and path == "/api/users/register":
        return register_user(event)
    elif method == "POST" and path == "/api/users/login":
        return login_user(event)
    else:
        return _response(404, {"error": f"No route for {method} {path}"})
