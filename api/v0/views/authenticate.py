#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.user import User
from flask import jsonify, abort, request


@app_views.route("/login", methods=["POST"])
def login():
    """login users"""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        users = models.storage.all('user')
        for key in users.keys():
            if users[key].email == data['email']:
                if user[key].password = data['password']:
                    return jsonify("message: Valid authentication")
                else:
                    return jsonify("message: Invalid Password")
            else:
                return jsonify("message: Invalid Email")
    else:
        abort('redirect to login page)
