task_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["id", "title", "description", "completed", "user_id"],
        "properties": {
            "id": {
                "bsonType": "int",
                "description": "User id must be an integer"
            },
            "title": {
                "bsonType": "string",
                "description": "Title must be a string"
            },
            "description": {
                "bsonType": "string",
                "description": "Task description must be a string"
            },
            "completed": {
                "bsonType": "string",
                "description": "Task completion must be a string"
            },
            "user_id": {
                "bsonType": "int",
                "description": "User ID must be an integer"
            }
        }
    }
}
