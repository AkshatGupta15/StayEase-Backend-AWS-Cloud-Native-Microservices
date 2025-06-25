import json
from cancellations import cancel_reservation
from utils import _response, extract_user_id

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
        if method == "POST" and path == "/api/cancellations":
            body_raw = event.get("body", "{}")
            body = json.loads(body_raw) if isinstance(body_raw, str) else body_raw

            user_id = extract_user_id(event)
            if not user_id:
                return _response(403, {"error": "Unauthorized or invalid token"})

            body["user_id"] = user_id
            return cancel_reservation(body)

        return _response(404, {"error": f"No route for {method} {path}"})

    except Exception as e:
        print("Exception in lambda_handler:", str(e))
        return _response(500, {"error": str(e)})
