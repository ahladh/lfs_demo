from kafka import KafkaConsumer
import yolo
import mongoDB
import storage_helper
import json
import os

consumer = KafkaConsumer('demo', bootstrap_servers="13.233.230.133:9092")

for msg in consumer:
    print(msg)
    data = json.loads(msg.value)
    key = data["blob_id"]
    storage_helper.download_file(key)
    analysis_report = yolo.analyze_image(key)
    mongoDB.save_objects_data(key,analysis_report)
    os.remove(key)

    
