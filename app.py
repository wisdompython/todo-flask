from flask import Flask, jsonify, request
from pymongo import MongoClient, ASCENDING
from tasks.crud import *
from users.schema import user_validator
from users.crud import *
from init_db import create_collection
app = Flask(__name__)

# connect to db

db = MongoClient("mongodb://taskdb:flaskdev_123!@mongo:27017/").new_db
db_task = create_collection(db=db, collection_name="task", validators=task_validator)
db_user = create_collection(db=db, collection_name="users", validators=user_validator)
db_user.create_index([("id", ASCENDING)], unique=True)
db_task.create_index([("id", ASCENDING)], unique=True)

@app.route("/task", methods=["POST"])
def add_task():
    task = create_task(db_task)
    return task


@app.route("/task", methods=["GET"])
def all_tasks():
    tasks = get_all_task(db_task)
    return jsonify({"tasks":str(tasks)})


@app.route("/task/<int:id>", methods=["GET"])
def retrieve_tasks(id):
    task = get_task(db_task, id)
    return jsonify(task)


@app.route("/task/<int:id>/", methods=["PATCH"])
def update_tasks(id):
    data = request.get_json()
    queryset_filter =  {"id": id}
    operation = {
        "$set": data
    }
    task = update_task(db_task, operation, queryset_filter)
    return jsonify(task)


@app.route("/users", methods=["POST"])
def add_user():
    user = create_user(db_user)
    return user

@app.route("/users/", methods=["GET"])
def retrieve_users(id):
    users = get_all_users(db_user, id)

    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET"])
def retrieve_users(id):
    user = get_user(db_user, id)

    return jsonify(user)

@app.route("users/<int:id>/task")
def get_user_task(id):
    pass

app.run(debug=True, host="0.0.0.0", port=8000)