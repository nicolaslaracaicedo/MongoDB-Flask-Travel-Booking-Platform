from flask import render_template, redirect, url_for, jsonify, request
from app.models.User import User
from app.services.UserService import UserService

class UserController:
    def __init__(self, environment):
        self.userService = UserService(environment)

    def create_user(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            password = request.form['password']
            address = request.form['address']
            # Assuming travel history is received as JSON and converted to Python list
            travel_history = request.json.get('travel_history', [])
            if name and email and password:
                self.userService.add_user(name, email, phone, password, address, travel_history)
                return redirect(url_for('list_users'))
            else:
                return jsonify({"error": "All fields are required"}), 400
        return render_template('User/create_user.html')

    def view_user(self, email):
        user = self.userService.get_user_by_email(email)
        if user:
            return render_template('User/view_user.html', user=user)
        else:
            return jsonify({"error": "User not found"}), 404

    def edit_user(self, email):
        if request.method == 'POST':
            new_name = request.form['name']
            new_phone = request.form['phone']
            new_password = request.form['password']
            new_address = request.form['address']
            if new_name or new_phone or new_password or new_address:
                if self.userService.update_user(email, new_name, new_phone, new_password, new_address):
                    return redirect(url_for('list_users'))
                else:
                    return jsonify({"error": "User not found"}), 404
            else:
                return jsonify({"error": "At least one field is required for update"}), 400
        user = self.userService.get_user_by_email(email)
        if user:
            return render_template('User/update_user.html', user=user)
        else:
            return jsonify({"error": "User not found"}), 404

    def delete_user(self, email):
        if self.userService.delete_user(email):
            return redirect(url_for('list_users'))
        else:
            return jsonify({"error": "User not found"}), 404
        
    def list_all_users(self):
        users = self.userService.get_all_users()
        return render_template('User/index.html', users=users)
