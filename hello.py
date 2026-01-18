from flask import Flask
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def pinnger():
    return {'Message': 'This is a Hello Message'}
