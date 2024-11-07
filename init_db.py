def create_collection(db, collection_name, validators):
    
    if collection_name not in db.list_collection_names():
        collection = db.create_collection(collection_name)
        db.command("collMod", collection_name, validator=validators)
        return collection
    else:
        db_collection = db[f"{collection_name}"]
        return db_collection