"""
Routes:
    * `/` - Redirects to `/app`
    * `/app/*` - Mostly UI, actual web pages
    * `/data/*` - API endpoints, for data purposes
"""
from datetime import datetime
from flask import Flask, redirect, jsonify


app = Flask(__name__, static_folder='public')


@app.route("/")
def home():
    return redirect("/app")


@app.route("/app/<path:path>")
def app_page(path):
    return


@app.route("/data/<path:path>")
def app_data(path):
    return jsonify(
        datetime=datetime.now(),
    )