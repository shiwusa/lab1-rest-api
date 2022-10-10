from flask import request, jsonify
import uuid1
from datetime import datetime
from rest_api.category import categories
from rest_api.user import users
from rest_api import app

records = []


@app.route("/record", methods=["POST"])
def create_record():
    record_id = uuid1.uuid1()
    request_record = request.get_json()
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
    return jsonify(records)


@app.route("/getUserRecord")
def get_user_record():
    user_ = request.get_json()["user_id"]
    user_records = [i for i in records if str(i["user_id"]) == user_]
    return jsonify(user_records)


@app.route("/getUserRecordCategory")
def get_user_record_cat():
    user_ = request.get_json()["user_id"]
    category_ = request.get_json()["category_id"]
    user_records_cat = [i for i in records if str(i["user_id"]) == user_ and str(i["category_id"]) == category_]
    return jsonify(user_records_cat)
