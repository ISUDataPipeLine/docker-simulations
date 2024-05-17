from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

def simulate_sensor_data():
    temperature = round(random.uniform(15.0, 30.0), 2)  # Simulate temperature in Celsius
    humidity = round(random.uniform(30.0, 70.0), 2)  # Simulate humidity in %
    return {
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': int(time.time())
    }

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    data = simulate_sensor_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

