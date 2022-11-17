from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

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
        user = UserModel(**user_request)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This name is already in use")
        return user
