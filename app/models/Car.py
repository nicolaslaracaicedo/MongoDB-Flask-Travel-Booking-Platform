class Car:
    def __init__(self, brand, model, year, price_per_day, availability, location, details):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.availability = availability
        self.location = location
        self.details = details

    def to_dict(self):
        return {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'price_per_day': self.price_per_day,
            'availability': self.availability,
            'location': self.location,
            'details': self.details
        }
