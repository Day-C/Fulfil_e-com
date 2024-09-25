#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.user import User
from flask import jsonify, abort, request

@app_views.route("/users")
def get_users():
    """retive list of users"""

    users = models.storage.all("user")

    users_list = []
    for key in users.keys():
        users_list.append(users[key].to_dict())
    return jsonify(users_list)

@app_views.route("/users/<user_id>")
def get_user(user_id):
    """retive specific user"""

    user = models.storage.get("user", user_id)
    if user != None:
        return jsonify(user.to_dict())
    else:
        abort(404)

@app_views.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """delete an existing user"""

    user = models.storage.get("user", user_id)
    if user != None:
        user.delete()
        return jsonify('{}')
    else:
        abort(404)

@app_views.route("/users/<user_id>", methods=["PUT"])
def edit_user(user_id):
    """make updates to an existing user"""

    user = models.storage.get("user", user_id)
    if user == None:
        abort(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(400)
    data = request.get_json()
    user_data = user
    for key in data.keys():
        user_data.__dict__[key] = data[key]
    user.delete()
    inst = User(**user_data.to_dict())
    inst.save()
    return jsonify(inst.to_dict())

@app_views.route("/users", methods=["POST"])
def create_user():
    """create a new user."""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        if 'email' not in data:
            abort(400, "Missing Email")
        if 'password' not in data:
            abort(400, "Missing Password")
        inst = User(**data)
        inst.save()
        return jsonify(inst.to_dict()), 201
    else:
        abort(404)
