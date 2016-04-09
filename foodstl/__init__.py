from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from werkzeug.contrib.fixers import ProxyFix

foodstl = Flask(__name__)
foodstl.wsgi_app = ProxyFix(foodstl.wsgi_app)

from routes import views
