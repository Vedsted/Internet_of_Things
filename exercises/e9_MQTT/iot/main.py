from umqtt import MQTTClient
import machine
import time

################################
# Connect to Broker
################################
device_name = 'IoT_Device'
broker_address = '192.168.1.115'
broker_port = 1883
topic = '/e9/temperature'

client = MQTTClient(device_name, broker_address, port=broker_port)

client.connect()


###############################
# Set up temperature measuring
##############################
adc = ADC()

blue_pin = adc.channel(pin='P16', attn=3) # Data pin (V_out pin on Thermistor), attn is the attenuation level
                                            # If attn=0, then the reading of the pin will be too high. attn=3 will lower the reading to the expected output from the thermistor.

p_red = Pin('P19', mode=Pin.OUT) # Use this pin to feed voltage to the Thermistor (V_dd pin on the Thermistor)
p_red.value(1) # Set the pin to HIGH i.e. output a current to the Thermistor

def cov_to_celc(x):
    return (0.08096044380894793*x-38.26863139396976)

##############################
# Measure temp and send messages
##############################

while True:
    temp = cov_to_celc(blue_pin())
    client.publish(topic=topic, msg='{\ntemp: %s,\nunit: c\n}' % str(temp))
    time.sleep(1)
