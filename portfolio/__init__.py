# -*- coding: utf-8 -*-

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app variable
app = Flask(__name__)

# Read and apply the config file
app.config.from_object(Config)

# Database instance
db = SQLAlchemy(app)
# Migration engine instance
migrate = Migrate(app, db)

# fro portfolio package
from portfolio import routes, models