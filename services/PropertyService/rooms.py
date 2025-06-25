from db import get_connection
from utils import _response, fix_dates

# --- ROOM ROUTES ---
def create_room(property_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO rooms (property_id, room_type, price_per_night, available, max_guests) "
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    property_id,
                    data["room_type"],
                    data["price_per_night"],
                    data.get("available", True),
                    data["max_guests"],
                ),
            )
            conn.commit()
            room_id = cur.lastrowid
            return _response(201, {"room_id": room_id})


def list_rooms(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM rooms WHERE property_id = %s", (property_id,))
            result = cur.fetchall()
            for row in result:
                fix_dates(row)
            return _response(200, result)


def get_room(property_id, room_id):
    print(">>> Fetching room:", room_id, "for property:", property_id)
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM rooms WHERE property_id = %s AND id = %s",
                (property_id, room_id),
            )
            result = cur.fetchone()
            print(">>> Result:", result)
            if result:
                fix_dates(result)
            return _response(200, result)

def update_room(property_id, room_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE rooms SET room_type = %s, price_per_night = %s, available = %s, max_guests = %s "
                "WHERE id = %s AND property_id = %s",
                (
                    data['room_type'],
                    data['price_per_night'],
                    data['available'],
                    data['max_guests'],
                    room_id,
                    property_id
                )
            )
            conn.commit()
            return _response(200, {"message": "Room updated"})

def delete_room(property_id, room_id):
    print(">>> Deleting room:", room_id, "for property:", property_id)
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM rooms WHERE id = %s AND property_id = %s",
                (room_id, property_id),
            )
            affected = cur.rowcount
            conn.commit()
            print(">>> Deleted rows:", affected)
            if affected == 0:
                return _response(404, {"error": "Room not found"})
            return _response(200, {"message": "Room deleted"})
