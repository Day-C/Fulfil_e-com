#!/usr/bin/python3
"""order api handler"""
import models
from . import app_views
from models/user import User
from models.order import Order

from flask import abort, jsonify, request

@app_views.route("/orders")
def get_orders():
    """retrive all orders."""

    orders = models.storage.all('order')
    order_list = []
    for key in orders.keys():
        order_list.append(orders[key].to_dict())
    return jsonify(order_list)

@app_views.route("/users/<user_id>/orders")
def get_users_orders(user_id):
    """retive specific user orders"""

    user = models.storage.get('user', user_id)
    if user != None:
        user_orders = []
        orders = models.storage.all('order')
        for key in orders.keys():
            if orders[key].__dict__['user_id'] == user_id:
                user_orders.append(orders[key].__dict__())
        return jsonify(user_orders)
    else:
        abort(404)

@app_views.route("/orders/<order_id>")
def get_order(order_id):
    """Retrive a single order"""

    order = models.storage.get('order', order_id)
    if order != None:
        return jsonify(order.to_dict())
    else:
        abort(404)

@app_views.route("/orders/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    """Deletee an existing order."""

    order = models.storage.get('order', order_id)
    if order != None:
        order.delete()
        return jsonify("{}")
    else:
        abort(404)

@app_views.route("/orders/<order_id>", methods=["PUT"])
def edit_order(order_id):
    """edit existing order"""

    order = models.storage.get('order', order_id)
    if order != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.gget_json()
            for key in data.keys():
                order.__dict__[key] = data[key]
            updated_order = order
            order.delete()
            updated_order.save()
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/users/<user_id>/order", methods=["POST"])
def create_order(user_id):
    """create a new order"""

    user = models.storage.get('user', user_id)
    if user != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            if 'products' not in data:
                abort(400)
            inst = Order(**data)
            inst.save()
            return jsonify(inst.to_dict()), 201
        else:
            abort(400)
    else:
        abort(404)
