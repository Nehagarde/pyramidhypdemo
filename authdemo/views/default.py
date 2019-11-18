from pyramid.compat import escape
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.view import view_config
import pickle
from .. import models
import json
# regular expression used to find WikiWords

@view_config(route_name='home',renderer="templates/home.jinja2")
def home(request):
    return {"content":"Hello"}

@view_config(route_name='login', renderer='json')                     #1
def login(request):
    print(request.json_body)

    #'data': pickle.dumps(request.params)
    return {'message':'inside after logging'}
    #return {'message': "yo mamma's so classless she could be a marxist utopia"}