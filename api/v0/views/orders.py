#!/usr/bin/python3
"""order api handler"""
import models
from . import app_views
from models.user import User
from models.product import Product
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
        orders = models.storage.all('order')
        for key in orders.keys():
            if orders[key].__dict__['user_id'] == user_id:
                return jsonify(orders[key].to_dict())
        abort(404)
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
            new_data = request.get_json()
            new_order = order
            for key in new_data.keys():
                new_order.__dict__[key] = new_data[key]
            order.delete()
            updated_order = Order(**new_order.to_dict())
            updated_order.save()
            return jsonify(updated_order.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/users/<user_id>/orders", methods=["POST"])
def create_order(user_id):
    """create a new order"""

    user = models.storage.get('user', user_id)
    if user != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            all_products = models.storage.all('product')
            ordered_products = []
            for key in data.keys():
                ordered_products.append(data[key])
            order_total = 0
            for i in range(len(ordered_products)):
                #clone product key
                product_key = 'Product.' + ordered_products[i]['id']
                if product_key in all_products:
                    prd = all_products[product_key]
                    order_total += prd.price * ordered_products[i]['quantity']
                    # print(order_total)
            order_details = {}
            order_details['user_id'] = user_id
            order_details['products'] = str(data)
            order_details['total'] = order_total
            #create order
            inst = Order(**order_details)
            print(inst)
            inst.save()
            return jsonify(inst.to_dict()), 201
        else:
            abort(400)
    else:
        abort(404)
