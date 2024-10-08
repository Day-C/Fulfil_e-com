#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.brand import Brand
from flask import jsonify, abort, request

@app_views.route("/brands")
def get_brands():
    """retive all brabds"""

    brands = models.storage.all('brand')
    brand_list = []
    for key in brands.keys():
        brand_list.append(brands[key].to_dict())
    return jsonify(brand_list)

@app_views.route("/brands/<brand_id>")
def get_brand(brand_id):
    """retivve a specific brand."""

    brand = models.storage.get('brand', brand_id)
    if brand != None:
        return jsonify(brand.to_dict())
    else:
        abort(404)

@app_views.route("/brands/<brand_id>", methods=["DELETE"])
def delete_brand(brand_id):
    """remove an exixting brand"""

    brand = models.storage.get('brand', brand_id)
    if brand != None:
        brand.delete()
    else:
        abort(404)

@app_views.route("/brands/<brand_id>", methods=["PUT"])
def edit_brand(brand_id):
    """eddit an existing brand"""

    brand = models.storage.get('brand', brand_id)
    if brand != None:
        if request.headers['Content-Type'] == 'application/json':
            new_data = request.get_json()
            brand_data = brand
            for key in new_data.keys():
                brand_data.__dict__[key] = new_data[key]
            brand.delete()
            edited_brand = Brand(**brand_data.to_dict())
            edited_brand.save()
            return jsonify(edited_brand.to_dict())
        abort(400)
    abort(404)

@app_views.route('/brands', methods=["POST"])
def create_brand():
    """Create a new brand"""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if 'name' not in data:
            abort(400)
        if 'category_id' not in data:
            abort(400)
        inst = Brand(**data)
        inst.save()
        return jsonify({}), 201
    else:
        abort(404)
