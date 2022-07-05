from flask import jsonify, request

from users import user_blueprint
from users.models import User
from app import db

@user_blueprint.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    if users:
        return jsonify(users)
    return jsonify('no user found for the moment')


@user_blueprint.route('/user', methods=['POST'])
def add_user():
    if request.is_json:
        name = request.json['name']
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return jsonify(user),201
    return jsonify('an error was occured')


@user_blueprint.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    user = User.query.filter_by(id=id_user).first()
    if user:
        User.query.filter_by(id=id_user).delete()
        db.session.commit()
        return jsonify('deleted'), 200
    return jsonify('user not exist'),409

