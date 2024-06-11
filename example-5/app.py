from flask import Flask, jsonify, request
from simulated_nodemcu import NodeMCUSimulator

app = Flask(__name__)
nodemcu = NodeMCUSimulator()

@app.route('/')
def index():
    return "Welcome to the NodeMCU Sensor Simulator!"

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    num_simulations = int(request.args.get('num', 1))
    data = [nodemcu.get_sensor_data() for _ in range(num_simulations)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

