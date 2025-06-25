from db import get_rooms_by_location as get_available_rooms
from availability import get_unavailable_room_ids
from utils import _response

def search_rooms(params):
    location = params.get("location")
    check_in = params.get("check_in")
    check_out = params.get("check_out")
    guests = int(params.get("guests", 1))

    if not (location and check_in and check_out):
        return _response(400, {"error": "Missing search parameters"})

    try:
        all_rooms = get_available_rooms(location, guests)
        room_ids = [room["room_id"] for room in all_rooms]
        unavailable = set(get_unavailable_room_ids(room_ids, check_in, check_out))
        available = [room for room in all_rooms if room["room_id"] not in unavailable]
        return _response(200, available)

    except Exception as e:
        print("Search error:", str(e))
        return _response(500, {"error": str(e)})
