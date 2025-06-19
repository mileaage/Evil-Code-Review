from flask import Flask
from .web.views import bp

def create_app():
    # create and config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
    )
    
    app.register_blueprint(bp)
    
    return app