from flask import Flask

app = Flask(__name__)

from rest_api.resources import user, category, record
from rest_api import views


