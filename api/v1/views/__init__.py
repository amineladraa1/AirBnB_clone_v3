#!/usr/bin/python3
"""__init__ file  of views package"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from .index import *
