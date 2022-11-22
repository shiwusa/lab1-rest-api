from flask import request
from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort

from flask.views import MethodView

from db import db
from models import RecordModel, UserModel, CategoryModel

from schemas import RecordSchema

blp = Blueprint("record", __name__, description="Records operations")


@blp.route("/record/<string:user_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self, user_id):
        record = RecordModel.query \
            .join(RecordModel.user) \
            .filter(UserModel.id == user_id) \
            .all()
        return record


@blp.route("/record")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        try:
            request_record = request.args
            user_id = request_record.get("user_id")
            category_id = request_record.get("category_id")
            query = RecordModel.query \
                .join(RecordModel.user) \
                .join(RecordModel.category) \
                .filter(UserModel.id == user_id) \
                .filter(CategoryModel.id == category_id)
            return query.all()
        except IntegrityError:
            abort(400, message="Record in such category not found")

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_record):
        record = RecordModel(**request_record)
        try:
            exist = CategoryModel.query \
                .join(CategoryModel.user) \
                .filter(CategoryModel.id == request_record.get["category_id"]) \
                .filter(CategoryModel.owner_id == request_record["user_id"]) \

            if len(exist.all()) > 0:
                db.session.add(record)
                db.session.commit()
            else:
                abort(400, message="No access to category")
        except IntegrityError:
            abort(400, message="Error while creating record")
        return record
