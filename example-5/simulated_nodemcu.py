# simulated_nodemcu.py
import random
import time

class DHTSensorSimulator:
    def read(self):
        temperature = round(random.uniform(15.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        return temperature, humidity

class NodeMCUSimulator:
    def __init__(self):
        self.sensor = DHTSensorSimulator()

    def get_sensor_data(self):
        temperature, humidity = self.sensor.read()
        return {
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': int(time.time())
        }


