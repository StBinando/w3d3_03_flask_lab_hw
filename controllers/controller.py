from flask import render_template
from our_app import flask_app
from models.fake_db import all_orders

@flask_app.route('/')
def index():
    return render_template("index.html", title = "All orders", my_orders = all_orders)

@flask_app.route('/order_<order_number>')
def single_order(order_number):

    chosen_order = chosen_order = [order for order in all_orders if order.order_number == order_number][0]
    return render_template("order_details.html", title = f"order #{order_number}", order = chosen_order)