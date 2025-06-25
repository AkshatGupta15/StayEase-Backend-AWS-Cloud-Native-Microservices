import boto3
import os

dynamo = boto3.resource("dynamodb")
table = dynamo.Table(os.environ["RESERVATIONS_TABLE"])

def fetch_reservation(reservation_id):
    response = table.get_item(Key={"reservation_id": reservation_id})
    return response.get("Item")

def update_reservation_status(reservation_id, status):
    table.update_item(
        Key={"reservation_id": reservation_id},
        UpdateExpression="SET #s = :val1",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":val1": status}
    )
