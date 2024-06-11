from app.models.User import User
from app.repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, environment):
        self.repository = UserRepository(environment)

    def agregar_usuario(self, username, email, password):
        self.repository.insertar_usuario(User(username, email, password))

    def obtener_usuario_por_email(self, email):
        return self.repository.obtener_usuario_por_email(email)

    def actualizar_usuario(self, email, nuevo_username=None, nuevo_password=None):
        return self.repository.actualizar_usuario(User('', email, ''), nuevo_username, nuevo_password)

    def eliminar_usuario(self, email):
        return self.repository.eliminar_usuario(User('', email, ''))
    def obtener_todos_los_usuarios(self):
        return self.repository.obtener_todos_los_usuarios()