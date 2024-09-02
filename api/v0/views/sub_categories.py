#!/usr/bin/python3
"""subcategory api handler"""
import models
from . import app_views
from models.subcategory import Subcategory
from flask import abort, jsonify, request

@app_views.route("/categories/<category_id>/subcategories")
def get_subcategs():
    """retrive all subcategories"""

    category = models.storage.get('category', category_id)
    if category == None:
        abort(404)
    subcat = models.storage.all('subcategory')
    subcat = []
    for key in subcat.keys():
        if subcat[key].__dict__['category_id'] == category_id:
            subcat.append(subcat[key].to_dict())

    return jsonify(subcat)

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

@app_views.route("/subcategorie/<subcategory_id>", methods=["PUT"])
def edit_subcateg(subcategory_id):
    """modify an existing subcategory."""

    subcategory = models.storage.get('subcategory', subcategory_id)
    if subcategory != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            for key in data.keys():
                subcategory.__dict__[key] = data[key]
            update = subcategory
            subcategory.delete()
            update.save()
            return jsonify(update.to_dict())
        else:
            abort(404)
    else:
        abort(404)

@appviews.route("/categories/<category_id>/subcategory", methods=["POST"])
def create_subcateg(category_id):
    """create a new subcategory"""

    category = models.storage.get('category', category_id)
    if category != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            if 'category_id' not in data:
                abort(400)
            if 'name' not in data:
                abort(400)
            inst = Subcategory(**data)
            inst.save()
        else:
            abort(400)
    else:
        abort(404)
