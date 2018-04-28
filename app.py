# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template
from jsonschema import validate
from twitter_api import TwitterApi
from weather import Weather
from thingspeak import ThingSpeak
import env
import json
import requests


app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', name='David')

@app.route('/api', methods=['POST'])
def publish_api():
    schema = {
        "type" : "object",
        "properties" : {
            "temperature" : {"type" : "number"},
            "humidity" : {"type" : "number"},
            "rain" : {"type" : "number"}
        }
    }

    try:
        params = json.loads(request.data)

        validate(params, schema)

        weather = Weather(params['temperature'], params['humidity'], params['rain'])
        weather.store()

        ts = ThingSpeak(params['temperature'], params['humidity'], params['rain'])
        ts.send()

        rain_msg = {
            0: 'não está chovendo',
            1: 'está caindo uma chuva fraca',
            2: 'chove muito'
        }[params['rain']]

        import random
        rand = random.randint(10,99)

        tweet = 'No momento fazem %.1fº, a humidade relativa do ar é de %d%% e %s' % (params['temperature'] + (rand / 100), params['humidity'], rain_msg)
        twitter = TwitterApi()
        twitter.publish(tweet)

        return jsonify({'message': 'sucesso'})
    except Exception as e:
        log = open('error.log', 'a')
        log.write('%s\n' % str(e))
        log.close()

        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.debug = True
    app.run()
