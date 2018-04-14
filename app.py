# -*- coding: utf-8 -*-

from flask import Flask, Response
import json
app = Flask(__name__)

@app.route('/')
def hello():
    data = {'message': 'Welcome to our api'}
    
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()
