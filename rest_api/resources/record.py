import uuid1
from flask_smorest import Blueprint, abort
from flask import request
from flask.views import MethodView
from datetime import datetime

from rest_api.resources.category import categories
from rest_api.resources.user import users
from rest_api.schemas import RecordSchema

blp = Blueprint("record", __name__, description="Records operations")

records = []


@blp.route("/record/<string:user_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self, user_id):
        try:
            user_records = [i for i in records if str(i["user_id"]) == user_id]
            return user_records
        except KeyError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        try:
            request_record = request.get_json()
            user_ = request_record["user_id"]
            category_ = request_record["category_id"]
            user_records_cat = [i for i in records if str(i["user_id"]) == user_
                                and str(i["category_id"]) == category_]
            return user_records_cat
        except KeyError:
            abort(404, message="Record in such category not found")

    @blp.response(200, RecordSchema)
    @blp.arguments(RecordSchema)
    def post(self, request_record):
        try:
            record_id = uuid1.uuid1()
            date = datetime.now()
            user_ = request_record["user_name"]
            category_ = request_record["category_title"]
            user_index = list(filter(lambda us: us["name"] == user_, users))
            cat_index = list(filter(lambda cat: cat["title"] == category_, categories))
            new_record = {
                "id": record_id,
                "user_id": user_index[0]["id"],
                "category_id": cat_index[0]["id"],
                "date": date.strftime("%d.%m.%Y %H:%M:%S"),
                "title": request_record["title"],
                "amount": request_record["amount"]
            }
            records.append(new_record)
            return new_record
        except KeyError:
            abort(404, message="Cannot create record with these fields")
