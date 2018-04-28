from datetime import datetime
import requests

class ThingSpeak(object):
    def __init__(self, temperature, humidity, rain):
        self.url = 'https://api.thingspeak.com/update'
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        self.data = {
            'api_key': 'RUXYNYJQJGCY7IZG',
            'field1': temperature,
            'field2': humidity,
            'field3': rain,
            'created_at': str(datetime.now())
        }

    def send(self):
        requests.post(self.url, headers=self.headers, data=self.data)

