# -*- coding: utf-8 -*-

from flask import Flask
from config import Configure
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config.from_object(Configure)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://user:password@url:5432/dbname"

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
