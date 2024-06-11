
from app.models.User import User
from app.repositories.UserRepository import UserRepository


class UserController:
    def __init__(self):
        self.repository = UserRepository()

    def crear_usuario(self, username, email, password):
        usuario = User(username, email, password)
        self.repository.insertar_usuario(usuario)

    def obtener_usuario_por_email(self, email):
        return self.repository.obtener_usuario_por_email(email)
