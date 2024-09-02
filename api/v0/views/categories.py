#!/usr/bin/python3
"""categoru api handler"""
import models
from . import app_views
from models.category import Category
from flask import jsonify, abort, request


@app_views.route("/categories")
def get_categories():
    """retrive all categories"""

    categories = models.storage.all('category')
    cat_list = []
    for key in categories.keys():
        cat_list.append(categories[key].to_dict())
    return jsonify(cat_list)

@app_views.route("/categories/<category_id>")
def get_category(category_id):
    """Retrive specific category."""

    category = models.storage.get('category', category_id)
    if category != None:
        return jsonify(categoty.to_dict())
    else:
        abort(404)

@app_views.route("/categories/<category_id>", methods=["DELETE"])
def delete_categ(category_id):
    """Remove an existing category"""

    category = models.storage.get('category', category_id)
    if category != None:
        category.delete()
        return jsonify({}), 200
    else:
        abort(404)

@app_views.route("/categories/<category_id>", methods=["PUT"])
def edit_categ(category_id):
    """modify an existing category"""

    category = models.storage.get('category', category_id)
    if category != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            for key in data.keys():
                category.__dict__[key] = data[key]
            updated_categ = category
            categoey.delete()
            updated_categ.save()
            return jsonify(updated_categ.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/categories", methods=["POST"])
def create_categ():
    """Create a new category."""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if 'name' not in data:
            abort(400)
        if 'description' not in data:
            abort(400)
        inst = Category(**data)
        inst.save()
        return jsonify(inst.to_dict()), 201
    else:
        abort(404)
