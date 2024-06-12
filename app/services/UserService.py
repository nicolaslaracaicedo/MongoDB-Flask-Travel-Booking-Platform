from app.models.User import User
from app.repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, environment):
        self.repository = UserRepository(environment)

    def add_user(self, name, email, phone, password, address, travel_history=None):
        user = User(name, email, phone, password, address, travel_history)
        self.repository.insert_user(user)

    def get_user_by_email(self, email):
        return self.repository.get_user_by_email(email)

    def update_user(self, email, new_name=None, new_phone=None, new_password=None, new_address=None):
        user = self.repository.get_user_by_email(email)
        if user:
            return self.repository.update_user(user, new_name, new_phone, new_password, new_address)
        return False

    def delete_user(self, email):
        user = self.repository.get_user_by_email(email)
        if user:
            return self.repository.delete_user(user)
        return False

    def get_all_users(self):
        return self.repository.get_all_users()
