# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Defining the secret key like this first checks for an environment variable,
    # if none is found, the 'default' key is passed
    # Key used to generate signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-hope-this-never-gets-guessed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

