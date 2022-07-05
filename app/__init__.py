from flask import Flask
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    #app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    
    
    from users import user_blueprint
    app.register_blueprint(user_blueprint)
    
    return app