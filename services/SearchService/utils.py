import pymysql
import os
import datetime
import json

def _response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def log_search(user_id, location, check_in, check_out):
    conn = pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        db=os.environ["DB_NAME"]
    )
    with conn.cursor() as cursor:
        query = """
            INSERT INTO search_logs (user_id, location_query, check_in_date, check_out_date, search_time, created_at)
            VALUES (%s, %s, %s, %s, NOW(), NOW())
        """
        cursor.execute(query, (user_id, location, check_in, check_out))
        conn.commit()
