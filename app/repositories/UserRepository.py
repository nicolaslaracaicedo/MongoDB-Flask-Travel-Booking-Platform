import pymongo

from app.models.User import User

class UserRepository:
    def __init__(self, environment):
        self.environment = environment
        self.cliente = pymongo.MongoClient(self.environment.get_database_url())
        self.db = self.cliente[self.environment.get_database_name()]
        self.coleccion = self.db["user"]

    def insertar_usuario(self, usuario):
        self.coleccion.insert_one(usuario.to_dict())

    def obtener_usuario_por_email(self, email):
        usuario_data = self.coleccion.find_one({'email': email})
        if usuario_data:
            return User(usuario_data['username'], usuario_data['email'], usuario_data['password'])
        return None

    def actualizar_usuario(self, usuario, nuevo_username=None, nuevo_password=None):
        update_data = {}
        if nuevo_username:
            update_data['username'] = nuevo_username
        if nuevo_password:
            update_data['password'] = nuevo_password

        if update_data:
            self.coleccion.update_one({'email': usuario.email}, {"$set": update_data})
            return True
        else:
            return False

    def eliminar_usuario(self, usuario):
        resultado = self.coleccion.delete_one({'email': usuario.email})
        return resultado.deleted_count > 0
import pymongo

class UserRepository:
    def __init__(self, environment):
        self.environment = environment
        self.cliente = pymongo.MongoClient(self.environment.get_database_url())
        self.db = self.cliente[self.environment.get_database_name()]
        self.coleccion = self.db["user"]

    def insertar_usuario(self, usuario):
        self.coleccion.insert_one(usuario.to_dict())

    def obtener_usuario_por_email(self, email):
        usuario_data = self.coleccion.find_one({'email': email})
        if usuario_data:
            return User(usuario_data['username'], usuario_data['email'], usuario_data['password'])
        return None

    def actualizar_usuario(self, usuario, nuevo_username=None, nuevo_password=None):
        update_data = {}
        if nuevo_username:
            update_data['username'] = nuevo_username
        if nuevo_password:
            update_data['password'] = nuevo_password

        if update_data:
            self.coleccion.update_one({'email': usuario.email}, {"$set": update_data})
            return True
        else:
            return False

    def eliminar_usuario(self, usuario):
        resultado = self.coleccion.delete_one({'email': usuario.email})
        return resultado.deleted_count > 0
    
    def obtener_todos_los_usuarios(self):
        usuarios = []
        for usuario_data in self.coleccion.find():
            usuarios.append(User(usuario_data['username'], usuario_data['email'], usuario_data['password']))
        return usuarios
