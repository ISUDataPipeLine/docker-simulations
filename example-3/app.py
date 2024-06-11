from flask import Flask, jsonify, request
from simulated_dht import DHTSensorSimulator
import time

app = Flask(__name__)
sensor = DHTSensorSimulator()

def simulate_sensor_data():
    temperature, humidity = sensor.read()
    return {
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': int(time.time())
    }

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    num_simulations = int(request.args.get('num', 1))
    data = [simulate_sensor_data() for _ in range(num_simulations)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


