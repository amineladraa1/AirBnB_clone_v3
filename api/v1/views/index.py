#!/usr/bin/python3
"""A file index, it contains route status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def status():
    """Return a Json response"""
    return jsonify({"status": "OK"}), 200


@app_views.route("/stats", strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    types = {"amenities": Amenity,  "cities": City,  "places": Place,
             "reviews": Review, "states": State, "users": User}
    json_dic = {}
    for key, value in types.items():
        json_dic[key] = storage.count(value)
    return jsonify(json_dic), 200
