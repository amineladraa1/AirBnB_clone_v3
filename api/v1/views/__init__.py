#!/usr/bin/python3
"""__init__ file  of views package"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
'''The blueprint for the AirBnB clone API.'''

from .index import *
from .states import *
