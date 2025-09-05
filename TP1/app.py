from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à Mongo (nom du service docker-compose = mongo)
client = MongoClient("mongodb://mongo:27017/")
db = client["ma_base"]
collection = db["messages"]

@app.route("/")
def hello():
    collection.insert_one({"msg": "Hello depuis Flask & Mongo 🚀"})
    return "Connexion réussie à MongoDB !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
