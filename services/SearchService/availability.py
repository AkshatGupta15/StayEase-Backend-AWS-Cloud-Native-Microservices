import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
from concurrent.futures import ThreadPoolExecutor

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["RESERVATIONS_TABLE"])

def check_conflict(room_id, check_in, check_out):
    try:
        response = table.query(
            KeyConditionExpression=Key("room_id").eq(room_id),
            FilterExpression=Attr("status").eq("confirmed") &
                             Attr("check_in").lt(check_out) &
                             Attr("check_out").gt(check_in)
        )
        return room_id if response.get("Items") else None
    except Exception as e:
        print(f"Error for room {room_id}: {e}")
        return None

def get_unavailable_room_ids(room_ids, check_in, check_out):
    print(f"Checking {len(room_ids)} rooms for availability")
    unavailable = set()

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda rid: check_conflict(rid, check_in, check_out), room_ids)
        for room_id in results:
            if room_id:
                unavailable.add(room_id)

    print(f"{len(unavailable)} rooms are booked")
    return unavailable
