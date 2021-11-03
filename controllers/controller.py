from flask import render_template
from our_app import flask_app
from models.fake_db import all_orders

@flask_app.route('/')
def index():
    return render_template("index.html", title = "Orders", my_orders = all_orders)