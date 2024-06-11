
from app.controllers.UserController import UserController


class UserService:
    def __init__(self):
        self.controller = UserController()

    def agregar_usuario(self, username, email, password):
        self.controller.crear_usuario(username, email, password)

    def obtener_usuario_por_email(self, email):
        return self.controller.obtener_usuario_por_email(email)
