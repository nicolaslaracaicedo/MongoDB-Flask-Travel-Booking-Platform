from flask import render_template, redirect, url_for, jsonify, request
from app.models.User import User
from app.services.UserService import UserService

class UserController:
    def __init__(self, environment):
        self.userService = UserService(environment)

    def crear_usuario(self):
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            if username and email and password:
                self.userService.agregar_usuario(username, email, password)
                return redirect(url_for('listar_usuarios'))
            else:
                return jsonify({"error": "Se requieren todos los campos"}), 400
        return render_template('User/crear_usuario.html')

    def ver_usuario(self, email):
        usuario = self.userService.obtener_usuario_por_email(email)
        if usuario:
            return render_template('User/ver_usuario.html', usuario=usuario)
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404

    def editar_usuario(self, email):
        if request.method == 'POST':
            nuevo_username = request.form['username']
            nuevo_password = request.form['password']
            if nuevo_username or nuevo_password:
                if self.userService.actualizar_usuario(email, nuevo_username, nuevo_password):
                    return redirect(url_for('listar_usuarios'))
                else:
                    return jsonify({"error": "Usuario no encontrado"}), 404
            else:
                return jsonify({"error": "Se requiere al menos un campo para actualizar"}), 400
        usuario = self.userService.obtener_usuario_por_email(email)
        if usuario:
            return render_template('User/actualizar_usuario.html', usuario=usuario)
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404

    def eliminar_usuario(self, email):
        if self.userService.eliminar_usuario(email):
            return redirect(url_for('listar_usuarios'))
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
        
    def listar_todos_los_usuarios(self):
        usuarios = self.userService.obtener_todos_los_usuarios()
        return render_template('User/index.html', usuarios=usuarios)
