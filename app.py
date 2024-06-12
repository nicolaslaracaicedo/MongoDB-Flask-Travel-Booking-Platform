# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from app.controllers.UserController import UserController
from app.config.Environment import Environment

app = Flask(__name__)
environment = Environment()
userController = UserController(environment)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    return userController.create_user()

@app.route('/users/<email>', methods=['GET'])
def view_user(email):
    return userController.view_user(email)

@app.route('/users/<email>/edit', methods=['GET', 'POST'])
def edit_user(email):
    return userController.edit_user(email)

@app.route('/users/<email>/delete', methods=['POST'])
def delete_user(email):
    return userController.delete_user(email)

@app.route('/users', methods=['GET'])
def list_users():
    return userController.list_all_users()

if __name__ == '__main__':
    app.run(debug=True)
