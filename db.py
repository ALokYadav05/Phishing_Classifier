from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://alokak:1973258@marketing-dev-mlmodel.grvcx8i.mongodb.net/?retryWrites=true&w=majority&appName=marketing-dev-mlmodel")

db = client["phishing_classifier"]   # Database name
collection = db["predictions"]       # Collection name

def save_prediction(url, features, prediction):
    data = {
        "url": url,
        "features": features,
        "prediction": prediction,
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(data)
