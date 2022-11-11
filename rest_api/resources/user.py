from flask_smorest import Blueprint, abort
from flask import request
from flask.views import MethodView
import uuid1


blp = Blueprint("user", __name__, description="User operations")

users = []


@blp.route("/user")
class UserList(MethodView):
    def get(self):
        return users

    def post(self):
        try:
            user_id = uuid1.uuid1()
            request_name = request.get_json()
            new_user = {
                "id": user_id,
                "name": request_name["name"]
            }
            users.append(new_user)
            return users
        except KeyError:
            abort(404, message="Cannot create user")