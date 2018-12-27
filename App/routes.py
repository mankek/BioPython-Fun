#!/usr/bin/python
from flask import Flask, render_template, url_for, request, jsonify, redirect
from App.methods import retrieve, preview, upload

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def db_query():
    if request.form["action"] == "query":
        db = request.form["database"]
        acc_num = request.form["id"]
        rettype = request.form["type"]
        retrieve(db, acc_num, rettype)
        return redirect(url_for("index"))
    elif request.form["action"] == "preview":
        db = request.form["database"]
        acc_num = request.form["id"]
        rettype = request.form["type"]
        result = preview(db, acc_num, rettype)
        return jsonify(result)


@app.route('/upload', methods=['POST'])
def file_upload():
    file_path = request.form["file"]
    upload(file_path)
    return redirect(url_for("index"))

