# reservations.py
import uuid
import json
from db import save_reservation_to_dynamo, fetch_reservation, is_room_already_booked
from ses_utils import send_booking_email
from utils import _response
from datetime import datetime
import boto3
import os


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["RESERVATIONS_TABLE"])

def create_reservation(data):
    try:
        print("Creating reservation with data:", data)

        required = ["user_id", "property_id", "room_id", "check_in", "check_out", "user_email"]
        for key in required:
            if key not in data:
                return _response(400, {"error": f"Missing field: {key}"})

        reservation_id = str(uuid.uuid4())
        item = {
            "reservation_id": reservation_id,
            "user_id": data["user_id"],
            "property_id": data["property_id"],
            "room_id": data["room_id"],
            "check_in": data["check_in"],
            "check_out": data["check_out"],
            "status": "confirmed",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if is_room_already_booked(data["room_id"], data["check_in"], data["check_out"]):
            return _response(409, {"error": "Room is already booked for the selected dates"})

        # Save to DynamoDB
        save_reservation_to_dynamo(item)

        # send_booking_email(data["user_email"], item)  # Uncomment if needed

        return _response(201, {"message": "Reservation created", "reservation_id": reservation_id})

    except Exception as e:
        print("Reservation creation failed:", str(e))
        return _response(500, {"error": str(e)})

def get_reservation(reservation_id):
    try:
        response = table.get_item(Key={"reservation_id": reservation_id})
        return response.get("Item")
    except Exception as e:
        print("Error in fetch_reservation:", str(e))
        raise