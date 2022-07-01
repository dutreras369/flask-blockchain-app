from flask import Blueprint,request,json
from flask import render_template

front = Blueprint("back", __name__)

@front.route('/')
def index():
    return render_template('index.html')