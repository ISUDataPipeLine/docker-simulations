# simulated_dht.py
import random

class DHTSensorSimulator:
    def read(self):
        temperature = round(random.uniform(15.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        return temperature, humidity


