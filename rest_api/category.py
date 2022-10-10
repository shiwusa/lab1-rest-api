from flask import request, jsonify
import uuid1
from rest_api import app

categories = []


@app.route("/category", methods=["POST"])
def create_category():
    category_id = uuid1.uuid1()
    request_title = request.get_json()
    new_category = {
        "id": category_id,
        "title": request_title["title"]
    }
    categories.append(new_category)
    return jsonify(categories)

