from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def main():
    return '<a href="/time">time</a>'

@app.route("/time")
def echo():
    return str(time.time())
