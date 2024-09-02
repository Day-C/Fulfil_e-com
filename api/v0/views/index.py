#!/usr/bin/python3
"""Api intro"""
from . import app_views
from flask import jsonify

@app_views.route("/status")
def status():
    """display api status"""

    status = {"status": "OK"}
    return jsonify(status), 200
