#!/bin/bash

# Stop existing Mosquitto container
docker stop mosquitto

# Remove old Mosquitto container
docker rm mosquitto

# Start Mosquitto MQTT broker
docker run -it -d \
	--name mosquitto \
	-p 1883:1883 \
	-p 9001:9001 \
	-v $PWD/mosquitto.conf:/mosquitto/config/mosquitto.conf \
	-v /mosquitto/data \
	-v /mosquitto/log \
	eclipse-mosquitto
