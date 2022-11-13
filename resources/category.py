from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import db
from models import CategoryModel
from schemas import CategorySchema

blp = Blueprint("category", __name__, description="Category operations")


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_title):
        category = CategoryModel(**request_title)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This category already exists")
        return category
