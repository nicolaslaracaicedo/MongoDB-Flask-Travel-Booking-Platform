class User:
    def __init__(self, name, email, phone, password, address, travel_history=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        self.travel_history = travel_history or []

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'address': self.address,
            'travel_history': self.travel_history
        }
