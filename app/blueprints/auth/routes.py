from app.blueprints.auth.models import User
from .import bp as app
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user, login_required
from app import db

#This will login the user
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #This is to find the user in the database 

        user = User.query.filter_by(email=email).first()

        #This is if the email and password don't match 

        if user is None or not user.check_password(password): 
            flash('Please enter a valid email or password', 'danger')
            return redirect(url_for('auth.login'))

            #Otherwise we log the user in
        login_user(user)
        flash('You have logged in successfully', 'info')
        return redirect(url_for('main.home'))
    return render_template('login.html')


#This will logout the User
@app.route('/logout')
def logout(): 
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('auth.login'))


#This will register the user
@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'POST': 
        user = User.query.filter_by(email=request.form.gt('email')).first()

        # This will check if the user already exists in the system
        if user is not None: 
            flash('User already exists. Please try another email address', 'warning')
            return redirect(url_for('auth.register'))

        #This checks if passwords match 
        if request.form.get('password') != request.form.get('confirm_password'): 
            flash('Your passwords do not match', 'danger')

        # This will create the user from the dict and save them in the system
        u = User()
        u.from_dict(request.form)
        u.save()
        flash('You have successfullly registered')
        return redirect(url_for('auth.login'))
    return render_template('register.html')
        

