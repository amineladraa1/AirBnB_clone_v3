#!/usr/bin/python3
""" Status of your API"""
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)
'''The Flask web application instance.'''
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.errorhandler(404)
def not_found(e):
    """404 error handling"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def call_storage(exception):
    """Close Session"""
    storage.close()


if __name__ == "__main__":
    HBNB_API_HOST = os.getenv('HBNB_API_HOST')
    HBNB_API_PORT = os.getenv('HBNB_API_PORT')
    host = HBNB_API_HOST if HBNB_API_HOST else '0.0.0.0'
    port = HBNB_API_PORT if HBNB_API_PORT else 5000
    app.run(host=host, port=port, threaded=True, debug=True)
