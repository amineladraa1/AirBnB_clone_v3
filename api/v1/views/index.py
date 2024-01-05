#!/usr/bin/python3
"""A file index, it contains route status"""
from api.v1.views import app_views
import json


@app_views.route("/status")
def status():
    """Return a Json response"""
    return json.dumps({"status": "OK"})
