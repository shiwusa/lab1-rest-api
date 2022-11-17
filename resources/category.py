from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import db
from models import CategoryModel, UserModel
from schemas import CategorySchema

blp = Blueprint("category", __name__, description="Category operations")


@blp.route("/category/<string:owner_id>")
class CategoryPrivate(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self, owner_id):
        try:
            category = CategoryModel.query \
                .join(CategoryModel.user) \
                .filter(UserModel.id == owner_id)
            return category.all()
        except IntegrityError:
            abort(400, message="Category is not available or does not exist")


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query \
            .filter(CategoryModel.private == 0).all()

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
