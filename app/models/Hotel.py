class Hotel:
    def __init__(self, name, location, rating, price_per_night, available_rooms, amenities, address, contact):
        self.name = name
        self.location = location
        self.rating = rating
        self.price_per_night = price_per_night
        self.available_rooms = available_rooms
        self.amenities = amenities
        self.address = address
        self.contact = contact

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'rating': self.rating,
            'price_per_night': self.price_per_night,
            'available_rooms': self.available_rooms,
            'amenities': self.amenities,
            'address': self.address,
            'contact': self.contact
        }
