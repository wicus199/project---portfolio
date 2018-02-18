# -*- coding: utf-8 -*-

from flask import Flask

# app variable
app = Flask(__name__)

# fro portfolio package
from portfolio import routes