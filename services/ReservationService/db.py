import boto3
import os
from boto3.dynamodb.conditions import Key, Attr


dynamo = boto3.resource("dynamodb")
table = dynamo.Table(os.environ["RESERVATIONS_TABLE"])

def save_reservation_to_dynamo(item):
    table.put_item(Item=item)
 
def fetch_reservation(reservation_id):
    response = table.get_item(Key={"id": reservation_id})
    return response.get("Item")

def is_room_already_booked(room_id, check_in, check_out):
    # Convert dates to ISO strings if needed
    check_in = str(check_in)
    check_out = str(check_out)

    # Scan or query all reservations for this room where status is 'confirmed'
    response = table.scan(
        FilterExpression=(
            Attr("room_id").eq(room_id) & 
            Attr("status").eq("confirmed") & 
            (
                (Attr("check_in").lt(check_out) & Attr("check_out").gt(check_in))
            )
        )
    )
    return len(response.get("Items", [])) > 0
