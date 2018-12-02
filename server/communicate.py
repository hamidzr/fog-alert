#!/bin/env python

"""
publishes detection of a threat to subscribers
"""

import paho.mqtt.client as paho
import time

# TODO refactor to use the config file?
BROKER = "broker.hivemq.com"
TOPIC = "hph/threat"

mqtt_client= paho.Client("detector-client")

def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))
"localhost" #
def trigger_response():
  print("publishing the threat")
  mqtt_client.publish(TOPIC,"detected")

# connect to the broker
print("connecting to broker ",BROKER)
mqtt_client.connect(BROKER)

# remember to close the connection on shutdown

if __name__ == '__main__':
  trigger_response()
  time.sleep(1)
  mqtt_client.disconnect()
