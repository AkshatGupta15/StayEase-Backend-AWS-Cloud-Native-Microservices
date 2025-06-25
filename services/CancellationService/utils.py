import json
import jwt

def _response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def extract_user_id(event):
    try:
        claims = event.get("requestContext", {}).get("authorizer", {}).get("jwt", {}).get("claims", {})
        if claims:
            return claims.get("sub")

        token = event["headers"].get("Authorization", "").split(" ")[-1]
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded.get("sub")

    except Exception as e:
        print("Token decode error:", str(e))
        return None
