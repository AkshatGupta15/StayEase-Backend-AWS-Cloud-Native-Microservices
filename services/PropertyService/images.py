from db import get_connection
from utils import _response
import boto3
from urllib.parse import quote_plus
import os

s3 = boto3.client("s3")
S3_BUCKET = os.environ["S3_BUCKET"]

def get_image_upload_url(property_id, room_id, filename):
    s3_key = f"rooms/{room_id}/{quote_plus(filename)}"
    upload_url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": S3_BUCKET,
            "Key": s3_key,
            "ContentType": "image/jpeg",
        },
        ExpiresIn=3600,
    )
    public_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}"
    return _response(200, {"upload_url": upload_url, "public_url": public_url})

def update_room_image_url(property_id, room_id, image_url):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE rooms SET image_url = %s WHERE id = %s AND property_id = %s",
                (image_url, room_id, property_id)
            )
            conn.commit()
            return _response(200, {"message": "Image URL updated"})