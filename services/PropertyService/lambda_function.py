# property_service.py
import os
import json
import pymysql
from datetime import datetime
from urllib.parse import quote_plus
import boto3

# --- ENVIRONMENT CONFIG ---
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']
S3_BUCKET = os.environ['S3_BUCKET']
s3 = boto3.client('s3')

# --- DB CONNECTION ---
def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

# --- UTIL ---
def _response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

# --- HANDLERS ---
def lambda_handler(event, context):
    method = event.get("httpMethod")
    path = event.get("path")
    body = json.loads(event.get("body", "{}"))
    params = event.get("pathParameters") or {}

    try:
        # Support both live API Gateway calls and manual test events
        method = event.get("httpMethod")
        path = event.get("path")
        body_raw = event.get("body", "{}")

        # Allow routeKey-based fallback for test events
        if not method or not path:
            route_key = event.get("routeKey")
            if route_key and " " in route_key:
                method, path = route_key.split(" ", 1)
            else:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({"error": "Missing or invalid routeKey"})
                }

        # Parse body safely (JSON string or dict)
        if isinstance(body_raw, str):
            body = json.loads(body_raw)
        else:
            body = body_raw

        # Also handle pathParameters (may be None)
        params = event.get("pathParameters") or {}

        # Property routes
        if method == "POST" and path == "/api/properties":
            return create_property(body)
        if method == "GET" and path == "/api/properties":
            return list_properties()
        if method == "GET" and path.startswith("/api/properties/") and len(params) == 1:
            return get_property(params['id'])
        if method == "PUT" and path.startswith("/api/properties/"):
            return update_property(params['id'], body)
        if method == "DELETE" and path.startswith("/api/properties/"):
            return delete_property(params['id'])


        # Room routes
# Create room under a property
if method == "POST" and path.endswith("/rooms") and "property_id" in params:
    return create_room(params["property_id"], body)

# List all rooms in a property
elif method == "GET" and path.endswith("/rooms") and "property_id" in params:
    return list_rooms(params["property_id"])

# Get single room
elif method == "GET" and path.endswith(f"/rooms/{params.get('id')}") and "property_id" in params and "id" in params:
    return get_room(params["property_id"], params["id"])

# Update room
elif method == "PUT" and path.endswith(f"/rooms/{params.get('id')}") and "property_id" in params and "id" in params:
    return update_room(params["property_id"], params["id"], body)

# Delete room
elif method == "DELETE" and path.endswith(f"/rooms/{params.get('id')}") and "property_id" in params and "id" in params:
    return delete_room(params["property_id"], params["id"])
        # Image upload
        if method == "POST" and path.endswith("/image-url"):
            return get_image_upload_url(params['property_id'], params['id'], body['filename'])
        if method == "PUT" and path.endswith("/image"):
            return update_room_image_url(params['property_id'], params['id'], body['image_url'])

        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": f"No route for {method} {path}"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }


# --- PROPERTY FUNCTIONS ---
def create_property(data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO properties (id, name, location, description, created_at) VALUES (%s, %s, %s, %s, %s)",
                        (data['id'], data['name'], data['location'], data.get('description', ''), datetime.utcnow()))
            conn.commit()
    return _response(201, {"message": "Property created"})

def list_properties():
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM properties")
            return _response(200, cur.fetchall())

def get_property(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM properties WHERE id = %s", (property_id,))
            result = cur.fetchone()
            if result:
                # Convert datetime fields to string
                for k, v in result.items():
                    if isinstance(v, datetime):
                        result[k] = v.isoformat()
            return _response(200, result)
            
def update_property(property_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE properties SET name=%s, location=%s, description=%s WHERE id=%s",
                        (data['name'], data['location'], data['description'], property_id))
            conn.commit()
            return _response(200, {"message": "Property updated"})

def delete_property(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM properties WHERE id = %s", (property_id,))
            conn.commit()
            return _response(200, {"message": "Property deleted"})

# --- ROOM FUNCTIONS ---
def create_room(property_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO rooms (property_id, room_type, price_per_night, available, max_guests) VALUES (%s, %s, %s, %s, %s)",
                        (property_id, data['room_type'], data['price_per_night'], data.get('available', True), data['max_guests']))
            conn.commit()
            room_id = cur.lastrowid
            return _response(201, {"room_id": room_id})

def list_rooms(property_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM rooms WHERE property_id = %s", (property_id,))
            return _response(200, cur.fetchall())

def get_room(property_id, room_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM rooms WHERE property_id = %s AND id = %s", (property_id, room_id))
            return _response(200, cur.fetchone())

def update_room(property_id, room_id, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE rooms SET room_type=%s, price_per_night=%s, available=%s, max_guests=%s WHERE id=%s AND property_id=%s",
                        (data['room_type'], data['price_per_night'], data['available'], data['max_guests'], room_id, property_id))
            conn.commit()
            return _response(200, {"message": "Room updated"})

def delete_room(property_id, room_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM rooms WHERE id = %s AND property_id = %s", (room_id, property_id))
            conn.commit()
            return _response(200, {"message": "Room deleted"})

# --- IMAGE HANDLING ---
def get_image_upload_url(property_id, room_id, filename):
    key = f"rooms/{room_id}/{quote_plus(filename)}"
    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={"Bucket": S3_BUCKET, "Key": key, "ContentType": "image/jpeg"},
        ExpiresIn=3600
    )
    public_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{key}"
    return _response(200, {"upload_url": url, "public_url": public_url})

def update_room_image_url(property_id, room_id, image_url):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE rooms SET image_url = %s WHERE id = %s AND property_id = %s", (image_url, room_id, property_id))
            conn.commit()
            return _response(200, {"message": "Image URL updated"})
