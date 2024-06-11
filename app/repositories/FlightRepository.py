import pymongo

from app.models.User import User

class UserRepository:
    def __init__(self):
        self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["nombre_de_tu_base_de_datos"]
        self.coleccion = self.db["nombre_de_tu_coleccion"]

    def insertar_usuario(self, usuario):
        self.coleccion.insert_one(usuario.to_dict())

    def obtener_usuario_por_email(self, email):
        usuario_data = self.coleccion.find_one({'email': email})
        if usuario_data:
            return User(usuario_data['username'], usuario_data['email'], usuario_data['password'])
        return None
