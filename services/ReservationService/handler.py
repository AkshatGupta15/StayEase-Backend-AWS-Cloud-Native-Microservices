# handler.py
import json
from reservations import create_reservation, get_reservation
from utils import _response
import jwt

def extract_user_id(event):
    try:
        # Preferred way with API Gateway JWT Authorizer
        claims = event.get("requestContext", {}).get("authorizer", {}).get("jwt", {}).get("claims", {})
        if claims:
            return claims.get("sub")  # or claims.get("email") if you prefer

        # Fallback for local tests or Lambda test events
        token = event["headers"].get("Authorization", "").split(" ")[-1]
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded.get("sub")

    except Exception as e:
        print("Token decode error:", str(e))
        return None
def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    method = event.get("httpMethod")
    path = event.get("path")

    # Fallback for test invoke / routeKey
    if not method or not path:
        route_key = event.get("routeKey", "")
        if " " in route_key:
            method, path = route_key.split(" ", 1)
        else:
            return _response(400, {"error": "Missing method/path or routeKey"})
    try:
        if method == "POST" and path == "/api/reservations":
            body_raw = event.get("body", "{}")
            body = json.loads(body_raw) if isinstance(body_raw, str) else body_raw

            user_id = extract_user_id(event)
            if not user_id:
                return _response(403, {"error": "Unauthorized or invalid token"})

            body["user_id"] = user_id  # override from token
            return create_reservation(body)

        elif method == "GET" and path.startswith("/api/reservations/"):
            reservation_id = event["pathParameters"]["id"]
            return get_reservation(reservation_id)

        return _response(404, {"error": f"No route for {method} {path}"})

    except Exception as e:
        print("Exception in lambda_handler:", str(e))
        return _response(500, {"error": str(e)})
