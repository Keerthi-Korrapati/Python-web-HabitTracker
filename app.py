from flask import Flask
from routes import pages
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # Getting .env file & load it into environment

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URL"))
    app.db = client.habitTracker

    app.register_blueprint(pages)
    return app