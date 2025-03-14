# data_ingestion_kafka.py
from kafka import KafkaConsumer
from pymongo import MongoClient
import json

def ingest_stream():
    # Initialize Kafka consumer to listen to the 'security_logs' topic
    consumer = KafkaConsumer(
        'security_logs',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["security_db"]
    collection = db["logs"]

    for message in consumer:
        log_entry = message.value
        # Clean and normalize log entry
        log_entry['log_message'] = log_entry.get('log_message', '').lower().strip()
        collection.insert_one(log_entry)
        print("Inserted log entry:", log_entry)

if __name__ == "__main__":
    ingest_stream()
