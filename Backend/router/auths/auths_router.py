from flask import Blueprint, request, jsonify
from provider.auths.login import login

auths_router = Blueprint('auths', __name__)


@auths_router.route('/logIn', methods=['POST'])
def handle_login():
    # Extracting Id and Password from request
    username = request.json.get('username')
    password = request.json.get('password')
    # Calling function "login"
    isSuccess, code, message = login(username, password)
    # Returning response
    if isSuccess:
        return jsonify({"pid": 1})
    else:
        return code, message
