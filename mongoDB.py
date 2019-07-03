import pymongo
import json

myclient = pymongo.MongoClient("mongodb://10.218.0.236:27017")
print(myclient.list_database_names())
image_analysis_db = myclient["ImageAnalysis"]
image_metadata_collection = image_analysis_db["ImageMetadata"]
records = image_metadata_collection.find({})
for record in records:
    print(record["_id"])

def save_objects_data(key, objects):
    """If record exists with the key then it updates the objects inside it
    else It will create a new record."""
    record = image_metadata_collection.find_one({"_id": key})
    print(record)
    if(record is None):
        print("inside if")
        record = {"_id":key, "objects": objects}
        image_metadata_collection.insert_one(record)
        return True
    else:
        print("inside else")
        record.extend(objects)
        updated_record = {"$set": { "objects": record["objects"] }}
        image_metadata_collection.update_one({"_id": key}, updated_record)
        return True
    return None

