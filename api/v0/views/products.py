#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.user import User
from flask import jsonity, abort, request


@app_views.route("/products")
def get_products():
    """retives all products."""

    products = models.storage.all('products')
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
    else:
        abort(404)

@app_views.route("/products/<product_id>", methods=["PUT"])
def edit_product(product_id):
    """modify and exixting product"""

    product = models.storage.get('product', product_id)
    if product != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            for key in data.keys():
                product.__dict__[key] = data[key]
            updated_prod  = product
            updated_prod.save()
            product.delete()
            return jsonify(updated_prod.to_dict())
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
    else:
        abort(400)
