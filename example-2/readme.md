## Example2:

Simulate multiple sets of data in a single request.

This modification allows you to generate and retrieve multiple sets of simulated temperature and humidity data in a single request.


Need to modify the app.py script (from 1st example)to generate and return an array of simulated data points.

The structure looks like this:

```
└── example-2

     ├── Dockerfile

     ├── app.py

     └── requirements.txt

```

## Explanation:

**Dockerfile**: Sets up a Python environment and runs app.py.

**requirements.txt**: Lists Flask as a dependency for creating a simple web server.

**app.py**: Simulates temperature and humidity data and serves it via a Flask web application.

in app.py:

**Query Parameter**: The number of simulations is controlled via the num query parameter. If num is not provided, it defaults to 1.

**Data Generation**: The simulate_sensor_data function is called multiple times to generate the requested number of data points.

**JSON Array**: The resulting data is returned as a JSON array, with each entry representing a single simulation result.


## Build and Run the Docker Container
Build the Docker image and run the container:

```
docker build -t nodemcu-simulation_2 .
```

This command will build the image using the Dockerfile in the current directory and tag it as nodemcu-simulation_2.

Run the docker container

```
docker run -d -p 8080:8080 nodemcu-simulation_2
```

## Test the Simulation

To get multiple sets of simulated data, specify the number of simulations using the num query parameter. For example, to get 5 sets of data, open your browser and navigate to:

```
http://localhost:8080/sensor?num=5

```