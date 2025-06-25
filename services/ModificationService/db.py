import boto3
import os
from boto3.dynamodb.conditions import Attr

dynamo = boto3.resource("dynamodb")
table = dynamo.Table(os.environ["RESERVATIONS_TABLE"])

def fetch_reservation(reservation_id):
    response = table.get_item(Key={"reservation_id": reservation_id})
    return response.get("Item")

def update_reservation(reservation_id, fields):
    update_expr = "SET " + ", ".join(f"#{k}=:{k}" for k in fields.keys())
    expr_attr_names = {f"#{k}": k for k in fields}
    expr_attr_values = {f":{k}": v for k, v in fields.items()}
    table.update_item(
        Key={"reservation_id": reservation_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_attr_names,
        ExpressionAttributeValues=expr_attr_values
    )

def check_conflict(room_id, check_in, check_out, exclude_id=None):
    response = table.scan(
        FilterExpression=(
            Attr("room_id").eq(room_id) &
            Attr("status").eq("confirmed") &
            Attr("reservation_id").ne(exclude_id) &
            Attr("check_in").lt(check_out) &
            Attr("check_out").gt(check_in)
        )
    )
    return len(response.get("Items", [])) > 0
