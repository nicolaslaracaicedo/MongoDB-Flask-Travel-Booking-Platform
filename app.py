# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from app.controllers.UserController import UserController
from app.config.Environment import Environment

app = Flask(__name__)
environment = Environment()
userController = UserController(environment)

@app.route('/', methods=['GET', 'POST'])
def inicio_sesion():
    return render_template('index.html')

@app.route('/usuarios/nuevo', methods=['GET', 'POST'])
def crear_usuario():
    return userController.crear_usuario()

@app.route('/usuarios/<email>', methods=['GET'])
def ver_usuario(email):
    return userController.ver_usuario(email)

@app.route('/usuarios/<email>/editar', methods=['GET', 'POST'])
def editar_usuario(email):
    return userController.editar_usuario(email)

@app.route('/usuarios/<email>/eliminar', methods=['POST'])
def eliminar_usuario(email):
    return userController.eliminar_usuario(email)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return userController.listar_todos_los_usuarios()

if __name__ == '__main__':
    app.run(debug=True)
