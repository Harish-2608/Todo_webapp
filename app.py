from flask import Flask, render_template, request, redirect, url_for
from operations import add_task, view_task, update_task, delete_task
import json_utiil

app = Flask(__name__)

@app.route("/")
def home():
    tasks = json_utiil.read_json()["task"]
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_desc = request.form["task_desc"]
    add_task(task_desc)
    return redirect(url_for("home"))

@app.route("/update/<int:task_id>")
def update(task_id):
    update_task(task_id)
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
