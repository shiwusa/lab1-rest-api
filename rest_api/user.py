from flask import request, jsonify
import uuid1
from rest_api import app

users = []


@app.route("/user", methods=["POST"])
def create_user():
    user_id = uuid1.uuid1()
    request_name = request.get_json()
    new_user = {
        "id": user_id,
        "name": request_name["name"]
    }
    users.append(new_user)
    return jsonify(users)
