import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
                  render_template, flash

# Create the actual application instance
app = Flask(__name__)
app.config.from_object('config') # Load config from this file.


