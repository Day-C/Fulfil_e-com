#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.product import Product
from flask import jsonify, abort, request


@app_views.route("/products")
def get_products():
    """retives all products."""

    products = models.storage.all('product')
    product_list = []
    for key in products.keys():
        product_list.append(products[key].to_dict())

    return jsonify(product_list)

@app_views.route("/products/<product_id>")
def get_product(product_id):
    """Retrive a single product"""

    product = models.storage.get('product', product_id)
    if product !=  None:
        return jsonify(product.to_dict())
    else:
        abort(404)

@app_views.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete an existing product"""

    product = models.storage.get('product', product_id)
    if product != None:
        product.delete()
        return jsonify('{}')
    else:
        abort(404)

@app_views.route("/products/<product_id>", methods=["PUT"])
def edit_product(product_id):
    """modify and exixting product"""

    product = models.storage.get('product', product_id)
    if product != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            new_product = product
            for key in data.keys():
                new_product.__dict__[key] = data[key]
            product.delete()
            updated_product = Product(**new_product.to_dict())
            updated_product.save()
            return jsonify(updated_product.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/products", methods=["POST"])
def create_product():
    """create a new product"""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if 'name' not in data:
            abort(404, "Missing name")
        if 'price' not in data:
            abort(404, "Missing price")
        if 'img_url' not in data:
            abort(404, "Missing img")
        inst = Product(**data)
        inst.save()
        return jsonify(inst.to_dict()), 201
    else:
        abort(400)
