#!/usr/bin/python3

import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World - Production v2 - NEW VERSION (Python)!!"

if __name__ == "__main__":
    app.run(debug=True, port=443)