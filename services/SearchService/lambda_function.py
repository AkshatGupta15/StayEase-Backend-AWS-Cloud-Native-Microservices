import json
from search import search_rooms
from utils import _response

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    try:
        # Support both REST and HTTP API Gateway formats
        method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method")
        path = event.get("path") or event.get("rawPath")

        if method == "GET" and path == "/api/search":
            params = event.get("queryStringParameters") or {}
            return search_rooms(params)

        elif method == "POST" and path == "/api/search":
            body_raw = event.get("body", "{}")
            body = json.loads(body_raw) if isinstance(body_raw, str) else body_raw
            return search_rooms(body)

        else:
            return _response(404, {"error": f"Invalid route {method} {path}"})

    except Exception as e:
        print("Error in Lambda handler:", str(e))
        return _response(500, {"error": str(e)})
