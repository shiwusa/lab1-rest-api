from flask import jsonify
from rest_api import app


@app.route("/")
def get():
    info = "laboratory work 1"
    return jsonify(info)
