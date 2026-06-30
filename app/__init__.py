# app/__init__.py
import os
from flask import Flask

# Use the package's default templates folder
app = Flask(__name__, template_folder='templates')