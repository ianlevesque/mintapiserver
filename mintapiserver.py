import os
import mintapi

from helpers import requires_auth

from flask import Flask, jsonify, request, Response
from flask.ext.cacheify import init_cacheify

app = Flask(__name__)
cache = init_cacheify(app)

class InvalidCredentials(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self)

@app.errorhandler(InvalidCredentials)
def handle_invalid_usage(error):
    return Response(error.message + '\n', 401, {'WWW-Authenticate': 'Basic realm="Mint credentials (retry)"'})

# def mintapi_token(username, password):
#     return mintapi.Mint(username, password).token

def mintapi_instance(username, password):
    try:
        mint = mintapi.Mint(username, password)
        # mint.token = mintapi_token(username, password)
        return mint
    except Exception, e:
        if 'login' in str(e):
            raise InvalidCredentials(str(e))
        else:
            raise

@cache.memoize(1800)
def fetch_accounts(username, password):
    return mintapi_instance(username, password).get_accounts()

@cache.memoize(1800)
def fetch_transactions(username, password):
    return mintapi_instance(username, password).get_transactions(False)

@app.route('/')
@requires_auth
def get_token():
    username = request.authorization.username
    password = request.authorization.password
    
    return jsonify(token=mintapi_instance(username,password).token)

@app.route('/accounts')
@requires_auth
def get_accounts():
    username = request.authorization.username
    password = request.authorization.password
    
    return jsonify(accounts=fetch_accounts(username,password))

@app.route('/transactions')
@requires_auth
def get_transactions():
    username = request.authorization.username
    password = request.authorization.password
    
    return Response(fetch_transactions(username,password).to_csv(index=False), 200, {'Content-Type': 'text/csv'})

if __name__ == '__main__':
    app.run(debug=True,port=8888)
