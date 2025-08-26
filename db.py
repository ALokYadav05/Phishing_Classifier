from pymongo import MongoClient
from dotenv import load_dotenv
import os, datetime

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["phishing_classifier"]
collection = db["predictions"]

def save_prediction(url, features, prediction):
    data = {
        "url": url,
        "features": features,
        "prediction": prediction,
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(data)
