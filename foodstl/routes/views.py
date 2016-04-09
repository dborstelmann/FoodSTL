from foodstl import foodstl
from flask import render_template, jsonify

@foodstl.route('/')
def landing():
    return render_template('landing.html')

@foodstl.route('/home')
def home():
    return render_template('home.html', data={})
