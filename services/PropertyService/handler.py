# handler.py
import json
from properties import create_property, get_property, update_property, delete_property, list_properties
from rooms import create_room, list_rooms, get_room, update_room, delete_room
from images import get_image_upload_url, update_room_image_url
from utils import _response

def lambda_handler(event, context):
    try:
        method = event.get("httpMethod")
        path = event.get("path")
        body_raw = event.get("body", "{}")
        params = event.get("pathParameters") or {}

        # Fallback to routeKey for test events
        if not method or not path:
            route_key = event.get("routeKey", "")
            if " " in route_key:
                method, path = route_key.split(" ", 1)
            else:
                return _response(400, {"error": "Missing or invalid routeKey"})

        # Parse body
        if isinstance(body_raw, str):
            body = json.loads(body_raw)
        else:
            body = body_raw

                # --- IMAGE ROUTES (most specific first!) ---
        if method == "POST" and path.endswith("/image-url") and "property_id" in params and "id" in params:
            return get_image_upload_url(params["property_id"], params["id"], body["filename"])

        if method == "PUT" and path.endswith("/image") and "property_id" in params and "id" in params:
            return update_room_image_url(params["property_id"], params["id"], body["image_url"])

        # --- ROOM ROUTES ---
        if method == "POST" and path.endswith("/rooms") and "property_id" in params:
            return create_room(params["property_id"], body)

        if method == "GET" and path.endswith("/rooms") and "property_id" in params:
            return list_rooms(params["property_id"])

        if method == "GET" and "/rooms/" in path and "property_id" in params and "id" in params:
            return get_room(params["property_id"], params["id"])

        if method == "PUT" and "/rooms/" in path and "property_id" in params and "id" in params:
            return update_room(params["property_id"], params["id"], body)

        if method == "DELETE" and "/rooms/" in path and "property_id" in params and "id" in params:
            return delete_room(params["property_id"], params["id"])

        # --- PROPERTY ROUTES (keep general ones last!) ---
        if method == "POST" and path == "/api/properties":
            return create_property(body)

        if method == "GET" and path == "/api/properties":
            return list_properties()

        if method == "GET" and path.startswith("/api/properties/") and "id" in params:
            return get_property(params["id"])

        if method == "PUT" and path.startswith("/api/properties/") and "id" in params:
            return update_property(params["id"], body)

        if method == "DELETE" and path.startswith("/api/properties/") and "id" in params:
            return delete_property(params["id"])


        # No route matched
        return _response(404, {"error": f"No route for {method} {path}"})

    except Exception as e:
        return _response(500, {"error": str(e)})
