class Flight:
    def __init__(self, origin, destination, departure_date, arrival_date, price, airline, available_seats, airplane_details):
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price = price
        self.airline = airline
        self.available_seats = available_seats
        self.airplane_details = airplane_details

    def to_dict(self):
        return {
            'origin': self.origin,
            'destination': self.destination,
            'departure_date': self.departure_date,
            'arrival_date': self.arrival_date,
            'price': self.price,
            'airline': self.airline,
            'available_seats': self.available_seats,
            'airplane_details': self.airplane_details
        }
