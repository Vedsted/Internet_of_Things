#! /bin/python
import paho.mqtt.client as mqtt
import time
from uptime import uptime

# Callback methods
def on_connect(client, userdata, flags, rc, properties=None):
    print('Connected to broker! Received ' + str(rc))

#   0: Connection successful
#   1: Connection refused - incorrect protocol version
#   2: Connection refused - invalid client identifier
#   3: Connection refused - server unavailable
#   4: Connection refused - bad username or password
#   5: Connection refused - not authorised
#   6-255: Currently unused. 

def on_publish(client, userdata, mid):
    print("Message published!")


# Set up connection
client_name = 'DesktopUptime'
topic = '/e9/uptime'
host_name = '192.168.1.115'
port = 1883

client = mqtt.Client(client_name)

# Define callbacks
client.on_connect = on_connect
client.connect(host_name, port=port)
client.on_publish = on_publish

client.loop_start()    #start the loop

while True:
    client.publish(topic, '{\n\ttime: %s,\n\tunit: "s"\n}' % str(uptime()))
    time.sleep(1)