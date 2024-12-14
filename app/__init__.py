from flask import Flask
from .config import Config
from .models import db
from .routes import bp  

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     db.init_app(app)  
#     app.register_blueprint(bp)  
    
#     return app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()  # This creates the tables based on the defined models
    
    app.register_blueprint(bp)
    
    return app