from foodstl import foodstl
from flask import render_template, jsonify

@foodstl.route('/')
def home():
    return render_template('home.html')
