import json
from datetime import datetime
from db import fetch_reservation, update_reservation, check_conflict
from utils import _response
import jwt

def extract_user_id(event):
    try:
        claims = event.get("requestContext", {}).get("authorizer", {}).get("jwt", {}).get("claims", {})
        return claims.get("sub")
    except Exception as e:
        print("Token decode error:", str(e))
        return None

def modify_reservation(event):
    try:
        user_id = extract_user_id(event)
        if not user_id:
            return _response(403, {"error": "Unauthorized or invalid token"})

        body = json.loads(event.get("body", "{}"))
        reservation_id = event["pathParameters"].get("reservation_id")

        if not reservation_id:
            return _response(400, {"error": "Missing reservation ID in path"})

        reservation = fetch_reservation(reservation_id)
        if not reservation:
            return _response(404, {"error": "Reservation not found"})

        if reservation["user_id"] != user_id:
            return _response(403, {"error": "Access denied: not your reservation"})

        # to only allow updates to check-in/check-out and room_id :::))) As Simple
        new_check_in = body.get("check_in", reservation["check_in"])
        new_check_out = body.get("check_out", reservation["check_out"])
        new_room_id = body.get("room_id", reservation["room_id"])

        if check_conflict(new_room_id, new_check_in, new_check_out, exclude_id=reservation_id):
            return _response(409, {"error": "Conflict: Room already booked for new dates"})

        updated_fields = {
            "check_in": new_check_in,
            "check_out": new_check_out,
            "room_id": new_room_id,
            "modified_at": datetime.utcnow().isoformat()
        }

        update_reservation(reservation_id, updated_fields)

        return _response(200, {"message": "Reservation modified", "reservation_id": reservation_id})

    except Exception as e:
        print("Modification error:", str(e))
        return _response(500, {"error": str(e)})
