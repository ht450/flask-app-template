from flask import Flask
from config import Config

# globally accessible libraries

def create_app(config_class=Config):
    """Initalise the core application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initalise plugins

    with app.app_context():

        # include our routes
        from app import views

        #functional
        from .views import home
        app.register_blueprint(home.bp)

        # divisional
        # register blueprints
        from .about import bp as about_bp
        app.register_blueprint(about_bp)

    return app
