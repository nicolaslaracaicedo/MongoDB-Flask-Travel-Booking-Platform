class Reservation:
    def __init__(self, user_id, reservation_type, reservation_details, reservation_date, status):
        self.user_id = user_id
        self.reservation_type = reservation_type
        self.reservation_details = reservation_details
        self.reservation_date = reservation_date
        self.status = status

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'reservation_type': self.reservation_type,
            'reservation_details': self.reservation_details,
            'reservation_date': self.reservation_date,
            'status': self.status
        }
