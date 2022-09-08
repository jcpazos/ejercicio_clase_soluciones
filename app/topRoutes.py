from app import app
import re
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser
import requests
import json

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")