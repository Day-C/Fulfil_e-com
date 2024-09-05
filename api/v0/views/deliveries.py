#!/usr/bin/python3
"""Delivery api handler"""
import models
from . import app_views
from models.delivery import Delivery
from flask import abort, request, jsonify


@app_views.route("/deliveries")
def get_deliveries():
    """retive all delivery"""

    deliveries = models.storage.all('delivery')
    delivery_list = []
    for key in deliveries.keys():
        delivery_list.append(deliveries[key].to_dict())
    return jsonify(delivery_list)

@app_views.route("deliveries/<delivery_id>")
def get_delivery(delivery_id):
    """retive a specific delivery."""

    delivery = models.storage.get('delivery', delivery_id)
    if delivery != None:
        return jsonify(delivery.to_dict())
    else:
        abort(404)

@app_views.route("/deliveries/delivery_id>", methods=["DELETE"])
def delete_delivery(delivery_id):
    """remove an exixting delivery"""

    delivery = models.storage.get('delivery', delivery_id)
    if delivery != None:
        delivery.delete()
    else:
        abort(404)

@app_views.route("/deliveries/<delivery_id>", methods=["PUT"])
def edit_delivery(delivery_id):
    """modify an existing delivery"""

    delivery = models.storage.get('delivery', delivery_id)
    if delivery != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            new_delivery = delivery
            for key in data.keys():
                new_delivery.__dict__[key] = data[key]
            delivery.delete()
            updated_delivery = Delivery(**new_delivery.to_dict())
            updated_delivery.save()
            return jsonify(updated_delivery.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/deliveries", methods=["POST"])
def create_Delivery():
    """Create a new delivery."""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if 'user_id' not in data:
            abort("Missing user_id", 400)
        if 'order_id' not in data:
            abort("Missing order_id", 400)
        inst = Delivery(**data)
        inst.save()
        return jsonify(inst.to_dict()), 201
    else:
        abort(404)
