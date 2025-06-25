import json
from modification import modify_reservation
from utils import _response

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    method = event.get("requestContext", {}).get("http", {}).get("method")
    path = event.get("rawPath")

    if method == "PATCH" and path.startswith("/api/modifications/"):
        return modify_reservation(event)

    return _response(404, {"error": f"No route for {method} {path}"})