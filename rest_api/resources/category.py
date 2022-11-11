import uuid1
from flask_smorest import Blueprint, abort
from flask import request
from flask.views import MethodView

blp = Blueprint("category", __name__, description="Category operations")
categories = []


@blp.route("/category")
class CategoryList(MethodView):
    def get(self):
        return categories

    def post(self):
        try:
            category_id = uuid1.uuid1()
            request_title = request.get_json()
            new_category = {
                "id": category_id,
                "title": request_title["title"]
            }
            categories.append(new_category)
            return categories
        except KeyError:
            abort(404, "Cannot create category")
