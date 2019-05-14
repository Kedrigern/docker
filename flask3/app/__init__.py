#!/usr/bin/env python3

import os

from flask import Flask
app = Flask(__name__)
from app import db
from app import views
