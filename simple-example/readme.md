## 1.st example:

This setup allows you to simulate the environment of a NodeMCU with a DHT (as an example) sensor using Docker, without needing any physical hardware.

The structure looks like this:

```
└── simple-example

     ├── Dockerfile

     ├── app.py

     └── requirements.txt

```

## Explanation:

**Dockerfile**: Sets up a Python environment and runs app.py.

**requirements.txt**: Lists Flask as a dependency for creating a simple web server.

**app.py**: Simulates temperature and humidity data and serves it via a Flask web application.

## Build and Run the Docker Container
Build the Docker image and run the container:

```
docker build -t <image_name>:<tag> <path_to_dockerfile>
```

**<image_name>**: Specifies the name of the image.

**tag**: (Optional) Specifies a tag for the image. If not provided, Docker assigns a default tag of latest.

**<path_to_dockerfile>**: Specifies the path to the directory containing the Dockerfile.


```
docker build -t nodemcu-simulation_1 .
```

This command will build the image using the Dockerfile in the current directory and tag it as nodemcu-simulation_1.

Run the docker container

```
docker run -d -p 8080:8080 nodemcu-simulation
```

## Test the Simulation
Open your web browser and navigate to http://localhost:8080/sensor to see the simulated temperature and humidity data.
