import boto3
import os

ses = boto3.client("ses", region_name="us-east-1")
FROM_EMAIL = os.environ["SES_SENDER_EMAIL"]

def send_booking_email(to_email, reservation):
    body = f"""Your reservation is confirmed!

Reservation ID: {reservation['reservation_id']}
Check-in: {reservation['check_in']}
Check-out: {reservation['check_out']}
"""
    ses.send_email(
        Source=FROM_EMAIL,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": "StayEase Reservation Confirmed"},
            "Body": {"Text": {"Data": body}}
        }
    )
