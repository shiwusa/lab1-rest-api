from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError
from flask import jsonify

from db import db
from models.user import UserModel
from schemas import UserSchema

blp = Blueprint("user", __name__, description="User operations")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_request):
        user = UserModel(
            name=user_request["name"],
            password=pbkdf2_sha256.hash(user_request["password"])
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This name is already in use")
        return user


@blp.route("/login")
class UserList(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_request):
        try:
            user = UserModel.query \
                .filter(UserModel.name == user_request["name"]).first()

            if user and pbkdf2_sha256.verify(user_request["password"], user.password):
                access_token = create_access_token(identity=user.id)
                return jsonify(access_token)
            else:
                abort(400, message="Wrong password")
        except IntegrityError:
            abort(400, message="User with this name does not exist")

