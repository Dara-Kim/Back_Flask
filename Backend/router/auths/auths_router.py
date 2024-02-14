from flask import Blueprint, request, jsonify
from provider.auths.login import LoginService

auths_router = Blueprint("auths", __name__)


@auths_router.route("/logIn", methods=["POST"])
def handle_login():
    username = request.json.get("username")
    password = request.json.get("password")

    Login = LoginService(username, password)
    pid = Login.login()

    return jsonify(
        {
            "pid": pid,
        }
    )
