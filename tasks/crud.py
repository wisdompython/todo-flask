import json
from bson import ObjectId
from flask import jsonify, request
from .schema import *
from jsonschema import validate, ValidationError
from pymongo.errors import *

def create_task(db):
    data = request.get_json()
    try:
        result = db.insert_one(data)
        return {"msg": "successfully added", "task_id": str(result.inserted_id)}, 200
    except WriteError as e:
        return jsonify({"error": f"Validation failed: {e}"}), 400

def get_all_task(db_task):
    tasks = list(db_task.find())
    for task in tasks:
        task["_id"] = str(task["_id"])    
    return {"tasks": tasks}

def get_task(db_task, id):
    result  = db_task.find_one({"id":id})
    result["_id"] = str(result["_id"])

   
    return {"task":result}


def update_task(db_task, operation, querset_filter):
    result = db_task.update_one(querset_filter, operation)
    if result.matched_count == 0:
        return {"error": "no match found"}
    return {"task":result.raw_result}