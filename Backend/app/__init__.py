from flask import Flask
# 기타 필요한 import 문

def create_app():
    app = Flask(__name__)
    # app.secret_key 설정 등

    from router.auths.auths_router import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/LogIn')

    return app