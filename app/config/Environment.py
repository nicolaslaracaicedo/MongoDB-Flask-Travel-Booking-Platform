import os
from dotenv import load_dotenv

class Environment:
    def __init__(self):
        load_dotenv()

    def get_database_name(self):
        return os.getenv("DB_NAME")

    def get_database_url(self):
        return os.getenv("DB_URL")