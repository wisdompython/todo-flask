import json
from bson import ObjectId
from flask import jsonify, request
from .schema import *
from pymongo.errors import *

def create_user(db):
    data = request.get_json()
    try:
        result = db.insert_one(data)
        return {"msg": "successfully added", "user_id": str(result.inserted_id)}, 200
    except WriteError as e:
        return jsonify({"error": f"Validation failed: {e}"}), 400

def get_all_users(db_task):
    tasks = list(db_task.find())
    for task in tasks:
        task["_id"] = str(task["_id"])    
    return {"users": tasks}

def get_user(db_task, id):
    result  = db_task.find_one({"id":id})
    result["_id"] = str(result["_id"])   
    return {"user":result}


def get_user_task(db_task, id):
    result  = db_task.find_many()
