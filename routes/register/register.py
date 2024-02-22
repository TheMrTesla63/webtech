from flask import Blueprint, render_template, request, redirect, url_for, flash
from filmfan import db
from models.user import User
from werkzeug.security import generate_password_hash

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please login.')
            return redirect(url_for('login'))
            
        existing_username = User.query.filter_by(username=username).first()
        if existing_user:
            flash('username already exists. Please login.')
            return redirect(url_for('login'))

        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(email=email, username=username, password=password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')
