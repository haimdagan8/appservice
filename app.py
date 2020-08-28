#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
<<<<<<< HEAD
    return "Hello World MASTER (Python)!"
=======
    return "Hello World - Final Version (Python)!"
>>>>>>> 7f81f8da20241cf6ba5a2715e57895c9243d6094

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=443)
