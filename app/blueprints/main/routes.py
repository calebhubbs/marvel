from flask import Blueprint, render_template
from flask_login import login_required
from .import bp as app

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/profile')
@login_required
def profile(): 
    return render_template('profile.html')
