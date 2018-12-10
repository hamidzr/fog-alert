# measure end to end performace
from camera.capture import snap, camera
from communication.communicate import post_file
import paho.mqtt.client as paho
import time
import signal
import sys

# config
STREAM_DELAY = 1 # sec
OUT_IMAGE = 'view.jpg' #output path

# TODO refactor to use the config file?
BROKER = 'broker.hivemq.com'
# BROKER = '10.0.0.14'
TOPIC = 'hph/threat'

def on_subscribe(client, userdata, mid, granted_qos):
  print("Subscribed: "+str(mid)+" "+str(granted_qos))

# will eat up exceptions w/o any warning
def on_message(client, userdata, msg):
  try:
    from time import time
    # global receive_time
    print(time(), 'received message =', str(msg.payload.decode('utf-8')))
    # receive_time = cur_time
    # print('diff', receive_time - init_time)
  except Exception as e:
    print(e)
    raise e


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(BROKER, 1883)
client.subscribe(TOPIC)
client.loop_start()


# setup teardown actions
def signal_handler(sig, frame):
  print('cleaning up before exit..')
  camera.stop_preview()
  client.loop_stop()
  client.disconnect()
  print('finished with cleanup')
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
  while True:
    print('starting..', time.time())
    # init_time =  start_time
    snap(OUT_IMAGE)
    print('posting the file')
    post_file(OUT_IMAGE)
    print('waiting')
    time.sleep(2)
