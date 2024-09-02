#!/usr/bin/python3
"""Delivery api handler"""
import models
from . import app_views
from models.delivery import Delivery
from flask import abort, request, jsnify


@app_view.route("/deliveries")
def get_deliveries():
    """retive all delivery"""

    deliveries = models.storage.all('drlivery')
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

@app_views.route("/deliveries/delivery_id>", methods=["PUT"])
def edit_delivery(delivery_id):
    """modify an existing delivery"""

    delivery = models.storage.get('delivery', delivery_id)
    if delivery != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            for key in data.keys():
                data.__dict__[key] = data[key]
            updated_delivery = delivery
            delivery.delete()
            updated_delivery.save()
            return jsonify(updated_delivery.to_dict())
        else:
            abort(400)
    else:
        abort(404)
