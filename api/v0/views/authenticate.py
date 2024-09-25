#!/usr/bin/python3
"""User api handler"""
import models
from . import app_views
from models.user import User
from flask import jsonify, abort, request, make_response


@app_views.route("/login", methods=["POST"])
def login():
    """login users"""
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        users_list = []
        users = models.storage.all('user')
        for key in users.keys():
            users_list.append(users[key])
        users = users_list
        print(len(users))
        for i in range(len(users)):
            if users[i].email == data['email']:
                print(users[i].password == data['password'])
                if users[i].password == data['password']:
                    # send a cookie
                    response = make_response(jsonify({"message": "Valid authentication"}))
                    response.set_cookie('urid',users[i].id)
                    return response
                else:
                    return abort(404, {"message": "Invalid Password"})
        return abort(404, {"message": "Invalid Email"})
    else:
        abort(400)

@app_views.route("/isauthenticated")
def isauthed():
    """Check cookies to see if user is already autenticated."""

    user_id = request.cookies.get('urid')
    if user_id:
        # return user_id
        return jsonify({'id': user_id})
    else:
        return jsonify({'id': 'None'})
