import os
import requests
from flask import Flask, session, render_template, request
from flask_session import Session

app = Flask(__name__)

@app.route('/')
def home():
    return """<h1>Printer Stats</h1>"""


if __name__ == '__main__':
    app.run('10.77.128.168', port=5000)


