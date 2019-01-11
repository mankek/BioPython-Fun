#!/usr/bin/python
from flask import Flask, render_template, url_for, request, jsonify, redirect
from App import methods

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    methods.get_files()
    return render_template("index.html", files=methods.global_record, prev="None")


@app.route('/query', methods=['POST'])
def db_query():
    if request.form["action"] == "query":
        db = request.form["database"]
        acc_num = request.form["id"]
        rettype = request.form["type"]
        methods.retrieve(db, acc_num, rettype)
        return redirect(url_for("index"))
    elif request.form["action"] == "preview":
        db = request.form["database"]
        acc_num = request.form["id"]
        rettype = request.form["type"]
        result = methods.preview(db, acc_num, rettype)
        return render_template("index.html", files=methods.global_record, prev=result)


@app.route('/upload', methods=['POST'])
def file_upload():
    file_path = request.form["file"]
    db = request.form["database"]
    methods.upload(file_path, db)
    return redirect(url_for("index"))


@app.route('/chart', methods=['POST'])
def show_chart():
    if request.form["action"] == "chart":
        title = request.form["charts"]
        file = request.form["filename"]
        file_type = request.form["filetype"]
        file_db = request.form["file"]
        if (title == "Nucleotide Composition") or (title == "Amino Acid Composition"):
            x_data, y_data = methods.comp(file, file_type, file_db)
            chart = "Bar"
        elif title == "GC Skew":
            x_data, y_data = methods.skew(file, file_type)
            chart = "Line"
        else:
            x_data = [0]
            y_data = [0]
            chart = "Bar"
        return render_template("BioP_chart.html", title=title, file=file, x=x_data, y=y_data, chart=chart)
    elif request.form["action"] == "previous":
        return redirect(url_for("index"))
