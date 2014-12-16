import os
import mintapi

from helpers import requires_auth

from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/accounts')
@requires_auth
def get_accounts():
    username = request.authorization.username
    password = request.authorization.password
    accounts = mintapi.get_accounts(username, password)
    return jsonify(accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True,port=8888)
