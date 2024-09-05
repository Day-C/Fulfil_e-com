#!/usr/bin/python3
"""order api handler"""
import models
from . import app_views
from models.user import User
from models.review import Review
from models.product import Product
from flask import abort, jsonify, request


@app_views.route("/products/<product_id>/reviews")
def get_reviews(product_id):
    """Retive all reviews"""

    product = models.storage.get('product', product_id)
    if product != None:
        product_reviews = []
        reviews = models.storage.all('review')
        for key in reviews.keys():
            if reviews[key].__dict__['product_id'] == product_id:
                product_reviews.append(reviews[key].to_dict())
        return jsonify(product_reviews)
    else:
        abort(404)

@app_views.route("/reviews/<review_id>")
def get_review(review_id):
    """Retive  a single review"""

    review = models.storage.get('review', review_id)
    if review != None:
        return jsonify(review.to_dict())
    else:
        abort(404)

@app_views.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """Delete  specific review"""

    review = models.storage.get('review', review_id)
    if review != None:
        review.delete(i)
        return jsonify('{}')
    else:
        abort(404)

@app_views.route("/reviews/<review_id>", methods=["PUT"])
def edit_review(review_id):
    """Edit existing review"""

    review = models.storage.get('review', review_id)
    if review != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            new_review = review
            for key in data.keys():
                new_review.__dict__[key] = data[key]
            review.delete()
            updated_review = Review(**new_review.to_dict())
            updated_review.save()
            return jsonify(updated_review.to_dict())
        else:
            abort(400)
    else:
        abort(404)

@app_views.route("/products/<product_id>/reviews", methods=["POST"])
def create_review(product_id):
    """Create new user"""

    product = models.storage.get('product', product_id)
    if product != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            data['product_id'] = product_id
            if 'user_id' not in data:
                abort("Missing user_id", 400)
            if "text" not in data:
                abort("Missing comment", 400)
            inst = Review(**data)
            inst.save()
            return jsonify(inst.to_dict()), 201
    else:
        abort(404)
