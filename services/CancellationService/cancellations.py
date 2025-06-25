from db import fetch_reservation, update_reservation_status
from utils import _response
from ses_utils import send_cancellation_email  

def cancel_reservation(data):
    try:
        reservation_id = data.get("reservation_id")
        user_id = data.get("user_id")

        if not reservation_id:
            return _response(400, {"error": "Missing reservation_id"})

        reservation = fetch_reservation(reservation_id)
        if not reservation:
            return _response(404, {"error": "Reservation not found"})

        # Authorization check
        if reservation["user_id"] != user_id and not data.get("is_admin", False):
            return _response(403, {"error": "Forbidden: You can't cancel this reservation"})

        if reservation["status"] == "cancelled":
            return _response(200, {"message": "Reservation already cancelled"})

        # Update status
        update_reservation_status(reservation_id, "cancelled")

        # Send cancellation email if user_email available
        to_email = data.get("user_email") or reservation.get("user_email")
        if to_email:
            send_cancellation_email(to_email, reservation_id)

        return _response(200, {"message": "Reservation cancelled successfully"})

    except Exception as e:
        print("Error cancelling reservation:", str(e))
        return _response(500, {"error": str(e)})
