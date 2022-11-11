import uuid1
from flask_smorest import Blueprint, abort
from flask import request
from flask.views import MethodView

from rest_api.schemas import CategorySchema

blp = Blueprint("category", __name__, description="Category operations")
categories = []


@blp.route("/category")
class CategoryList(MethodView):
    def get(self):
        return categories

    @blp.arguments(CategorySchema)
    def post(self, request_title):
        try:
            if any(cat["title"] == request_title["title"] for cat in categories):
                abort(400, message="This category already exists")
            category_id = uuid1.uuid1()
            new_category = {
                "id": category_id,
                "title": request_title["title"]
            }
            categories.append(new_category)
            return categories
        except KeyError:
            abort(404, "Cannot create category")
