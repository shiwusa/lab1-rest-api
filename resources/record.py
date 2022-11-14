from flask import request
from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort

from flask.views import MethodView

from db import db
from models import RecordModel, UserModel, CategoryModel

from schemas import RecordSchema

blp = Blueprint("record", __name__, description="Records operations")


@blp.route("/record/<string:user_name>")
class Record(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self, user_name):
        record = RecordModel.query\
            .join(RecordModel.user) \
            .filter(UserModel.name == user_name)\
            .all()
        return record


@blp.route("/record")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        try:
            request_record = request.get_json()
            user_name = request_record["user_name"]
            category_title = request_record["category_title"]
            query = RecordModel.query \
                .join(RecordModel.user) \
                .join(RecordModel.category) \
                .filter(UserModel.name == user_name) \
                .filter(CategoryModel.title == category_title)
            return query.all()
        except IntegrityError:
            abort(400, message="Record in such category not found")

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_record):
        record = RecordModel(**request_record)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error while creating record")
        return record
