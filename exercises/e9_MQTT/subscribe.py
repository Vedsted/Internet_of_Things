#! /bin/python
import paho.mqtt.client as mqtt
import time

# callback when messages are received
def on_message(client, userdata, message):
    print("\nmessage received!")
    print("topic= ",message.topic)
    print(str(message.payload.decode("utf-8")))



# Set up connection
client_name = 'Subscriber'
topic = '/e9/temperature'
broker_address = '192.168.43.62'
port = 1883

client = mqtt.Client(client_name)
client.on_message = on_message

client.connect(broker_address, port=port)
client.loop_start()    #start the loop
client.subscribe(topic)

x = input() # End program when input is received
client.loop_stop()    #stop the loop