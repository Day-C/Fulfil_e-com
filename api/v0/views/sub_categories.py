#!/usr/bin/python3
"""subcategory api handler"""
import models
from . import app_views
from models.subcategory import Subcategory
from flask import abort, jsonify, request

@app_views.route("/categories/<category_id>/subcategories")
def get_subcategs(category_id):
    """retrive all subcategories"""

    category = models.storage.get('category', category_id)
    if category == None:
        abort(404)
    subcat = models.storage.all('subcategory')
    cat_subcat = []
    for key in subcat.keys():
        if subcat[key].__dict__['category_id'] == category_id:
            cat_subcat.append(subcat[key].to_dict())

    return jsonify(cat_subcat)

@app_views.route("/subcategories/<subcategory_id>")
def get_subcateg(subcategory_id):
    """retive a single subcategory."""

    subcat = models.storage.get('subcategory')
    if subcat != None:
        return jsonify(subcat.to_dict())
    else:
        abort(404)

@app_views.route("/subcategories/<subcategory_id>", methods=['DELETE'])
def delete_subcateg(subcategory_id):
    """delete a subcategoory."""

    subcategory = models.storage.get('subcategory', subcategory_id)
    if subcategory != None:
        subcategory.delete()
    else:
        abort(404)

@app_views.route("/subcategories/<subcategory_id>", methods=["PUT"])
def edit_subcateg(subcategory_id):
    """modify an existing subcategory."""

    subcategory = models.storage.get('subcategory', subcategory_id)
    if subcategory != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            new_sub_cat = subcategory
            for key in data.keys():
                new_sub_cat.__dict__[key] = data[key]
            subcategory.delete()
            updated_sub_categ =  Subcategory(**new_sub_cat.to_dict())
            updated_sub_categ.save()
            return jsonify(updated_sub_categ.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/categories/<category_id>/subcategory", methods=["POST"])
def create_subcateg(category_id):
    """create a new subcategory"""

    category = models.storage.get('category', category_id)
    if category != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            data['category_id'] = category_id
            if 'name' not in data:
                abort(400)
            inst = Subcategory(**data)
            inst.save()
            return jsonify(inst.to_dict()), 201
        else:
            abort(400)
    else:
        abort(404)
