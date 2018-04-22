# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Welcome to our api'})

@app.route('/api', methods=['POST'])
def call_api():
    return jsonify({'message': 'Success!'})

if __name__ == '__main__':
    app.debug = True
    app.run()
