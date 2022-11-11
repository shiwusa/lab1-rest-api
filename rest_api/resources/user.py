from flask_smorest import Blueprint, abort
from flask.views import MethodView
import uuid1

from rest_api.schemas import UserSchema

blp = Blueprint("user", __name__, description="User operations")

users = []


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return users

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema(many=True))
    def post(self, user_request):
        try:
            if any(u["name"] == user_request["name"] for u in users):
                abort(400, message="This name is already in use")
            user_id = uuid1.uuid1()
            new_user = {
                "id": user_id,
                "name": user_request["name"]
            }
            users.append(new_user)
            return users
        except KeyError:
            abort(404, message="Cannot create user")