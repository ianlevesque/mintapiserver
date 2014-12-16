import os
import mintapi

from helpers import requires_auth

from flask import Flask, jsonify, request, Response
from flask.ext.cacheify import init_cacheify

app = Flask(__name__)
cache = init_cacheify(app)

@cache.memoize(1800)
def get_accounts_from_mint(username, password):
    return mintapi.get_accounts(username, password)

@app.route('/accounts')
@requires_auth
def get_accounts():
    username = request.authorization.username
    password = request.authorization.password
    
    accounts = get_accounts_from_mint(username, password)
    return jsonify(accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True,port=8888)
