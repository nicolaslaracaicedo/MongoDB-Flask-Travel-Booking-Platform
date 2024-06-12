import pymongo
from app.models.User import User

class UserRepository:
    def __init__(self, environment):
        self.environment = environment
        self.client = pymongo.MongoClient(self.environment.get_database_url())
        self.db = self.client[self.environment.get_database_name()]
        self.collection = self.db["users"]

    def insert_user(self, user):
        self.collection.insert_one(user.to_dict())

    def get_user_by_email(self, email):
        user_data = self.collection.find_one({'email': email})
        if user_data:
            return User(
                name=user_data['name'],
                email=user_data['email'],
                phone=user_data['phone'],
                password=user_data['password'],
                address=user_data['address'],
                travel_history=user_data.get('travel_history', [])
            )
        return None

    def update_user(self, user, new_name=None, new_phone=None, new_password=None, new_address=None):
        update_data = {}
        if new_name:
            update_data['name'] = new_name
        if new_phone:
            update_data['phone'] = new_phone
        if new_password:
            update_data['password'] = new_password
        if new_address:
            update_data['address'] = new_address

        if update_data:
            self.collection.update_one({'email': user.email}, {"$set": update_data})
            return True
        else:
            return False

    def delete_user(self, user):
        result = self.collection.delete_one({'email': user.email})
        return result.deleted_count > 0

    def get_all_users(self):
        users = []
        for user_data in self.collection.find():
            users.append(User(
                name=user_data['name'],
                email=user_data['email'],
                phone=user_data['phone'],
                password=user_data['password'],
                address=user_data['address'],
                travel_history=user_data.get('travel_history', [])
            ))
        return users
