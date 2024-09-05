#!/usr/bin/python3
"""Api views"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v0')

from .index import *
from .users import *
from .brands import *
from .categories import *
from .orders import *
from .deliveries import *
from .sub_categories import *
from .reviews import *
from .products import *
