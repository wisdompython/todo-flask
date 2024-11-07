user_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["id", "email", "username"],
        "properties": {
            "id": {
                "bsonType": "int",
                "description": "User id must be an integer"
            },
            "username": {
                "bsonType": "string",
                "description": "Username must be a string"
            },
            "email": {
                "bsonType": "string",
                "description": "User email must be a string"
            }
        }
    }
}