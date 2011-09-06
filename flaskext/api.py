# -*- coding: utf-8 -*-
"""
    flaskext.api
    ~~~~~~~~~~~~~~~~~

    Flask-API allow to easily build and publish an API for a Flask application
       
    :copyright: 2011 by Nicolas Clairon <n.namlook+flaskapi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

from flask import Response, request
from time import time
import traceback
from flask import current_app

class ArgumentError(Exception):pass

def _get_args(required, optional):
    apiargs = {}
    request_args = json.loads(request.args.get('q'), object_hook=current_app.config.get('JSON_OBJECT_HOOK', None))#json_util.object_hook)
    ## handle required arguments
    for arg in required:
        if arg not in request_args:
            raise ArgumentError('"%s" not found and required' % arg)
        apiargs[arg] = request_args[arg]
    ## handle optionals argumens
    for arg, value in optional.iteritems():
        print arg, request_args
        if arg in request_args:
            apiargs[arg] = request_args[arg]
        else:
            apiargs[arg] = optional[arg]
    return apiargs

from functools import wraps
def api(required=None, optional=None):
    if required is None:
        required = {}
    if optional is None:
        optional = {}
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            results = {'status': None, 'result': None}
            start = time()
            try:
                apiargs = _get_args(required, optional)
                results['status'] = 'ok'
                results['result'] = f(**apiargs)
            except Exception, e:
                results['status'] = e.__class__.__name__
                results['result'] = unicode(e)
                print traceback.format_exc()
            finish = time()
            results['time'] = finish-start
            return Response(
              json.dumps(results, default=current_app.config.get('JSON_DEFAULT', None)),#json_util.default),
              content_type = 'application/json'
            )
        return decorated_function
    return decorator


#
# Api Client
#

from apibee import Client as ApiBeeClient
import json

class ApiError(Exception): pass

class Http404(Exception): pass
class NotFound(Http404):pass

class Http401(Exception): pass
class NotAuthorized(Http401):pass

class Http403(Exception): pass
class Forbiden(Http403): pass

exceptions = {}
for exception in [Http401, Http403, Http404, NotFound, NotAuthorized, Forbiden]:
    exceptions[exception.__name__] = exception

class Client(ApiBeeClient):

    def set_persistent_query(self, **args):
        self._persistent_query = args
    
    def build_request(self, resource, query):
        query = {'q': json.dumps(query)}
        query.update(self._persistent_query)
        return resource, query

    def process_result(self, result):
        result = json.loads(result)
        if result['status'] != 'ok':
            if result['status'] in exceptions:
                raise exceptions[result['status']](result['result'])
            raise ApiError('%s: %s' % (result['status'], result['result']))
        return result


