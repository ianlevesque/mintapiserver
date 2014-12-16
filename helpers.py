from functools import wraps
from flask import request, Response

def authenticate():
    return Response('Provide Mint username & password\n\n', 401, {'WWW-Authenticate': 'Basic realm="Mint credentials"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.authorization:
            return authenticate()
        return f(*args, **kwargs)
    return decorated
