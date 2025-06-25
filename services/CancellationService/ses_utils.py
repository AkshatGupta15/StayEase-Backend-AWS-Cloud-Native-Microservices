import boto3
import os

ses = boto3.client("ses", region_name="us-east-1")
FROM_EMAIL = os.environ["SES_SENDER_EMAIL"]

def send_cancellation_email(to_email, reservation_id):
    body = f"Your reservation {reservation_id} has been cancelled."
    ses.send_email(
        Source=FROM_EMAIL,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": "StayEase Reservation Cancelled"},
            "Body": {"Text": {"Data": body}}
        }
    )
