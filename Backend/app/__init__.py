from flask import Flask

def register_router(flask_app: Flask):
    from router.auths.auths_router import auths_router

    flask_app.register_blueprint(auths_router, url_prefix='/auths')
    
def create_app():
    app = Flask(__name__)
    register_router(app)
    return app