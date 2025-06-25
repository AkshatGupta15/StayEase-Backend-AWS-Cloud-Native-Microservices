# properties.py
from db import get_connection
from utils import _response, fix_dates
from datetime import datetime

# --- PROPERTY ROUTES ---
def create_property(data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO properties (id, name, location, description, created_at) VALUES (%s, %s, %s, %s, %s)",
                (data['id'], data['name'], data['location'], data.get('description', ''), datetime.utcnow())
            )
            conn.commit()
    return _response(201, {"message": "Property created"})

def list_properties():
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM properties")
            results = cur.fetchall()
            for row in results:
                fix_dates(row)
            return _response(200, results)

def get_property(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM properties WHERE id = %s", (property_id,))
            result = cur.fetchone()
            if result:
                fix_dates(result)
            return _response(200, result)

def update_property(property_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE properties SET name = %s, location = %s, description = %s WHERE id = %s",
                (data['name'], data['location'], data['description'], property_id)
            )
            conn.commit()
            return _response(200, {"message": "Property updated"})

def delete_property(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM properties WHERE id = %s", (property_id,))
            conn.commit()
            return _response(200, {"message": "Property deleted"})