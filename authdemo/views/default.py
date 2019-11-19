from pyramid.compat import escape
import re
from docutils.core import publish_parts
from authdemo.models.user import User
from pyramid.security import (
    remember,
    forget,
    )
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
    uname = request.json_body['uname']
    passwd = request.json_body['passwd']
    user = request.dbsession.query(User).filter_by(name=login).first()
    if user is not None and user.check_password(passwd):
        headers = remember(request, user.id)
        return {'message':"Loggedin","headers":headers,"role":user.role}

    message = 'Failed login'
    #'data': pickle.dumps(request.params)
    return {'message':message}
    #return {'message': "yo mamma's so classless she could be a marxist utopia"}