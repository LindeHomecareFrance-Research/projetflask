from flask import Blueprint

user_blueprint = Blueprint('user_blueprint',__name__)
from users import routes