import pymysql
import os

def get_db_conn():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        db=os.environ["DB_NAME"],
        cursorclass=pymysql.cursors.DictCursor
    )

def get_rooms_by_location(location, guests):
    conn = get_db_conn()
    with conn.cursor() as cursor:
        query = """
            SELECT r.id AS room_id, r.room_type, r.price_per_night, r.max_guests,
                   p.id AS property_id, p.name AS property_name, p.location
            FROM rooms r
            JOIN properties p ON r.property_id = p.id
            WHERE p.location LIKE %s AND r.max_guests >= %s
        """
        cursor.execute(query, [f"%{location}%", guests])
        return cursor.fetchall()

def get_conflicting_bookings(check_in, check_out):
    conn = get_db_conn()
    with conn.cursor() as cursor:
        query = """
            SELECT room_id FROM bookings
            WHERE status = 'confirmed'
              AND NOT (check_out <= %s OR check_in_date >= %s)
        """
        cursor.execute(query, (check_in, check_out))
        return cursor.fetchall()
