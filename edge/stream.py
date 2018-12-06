from camera.capture import snap, camera
from communication.communicate import post_file
import time
import signal
import sys

print('done with imports')

# config
STREAM_DELAY = 2 # sec
OUT_IMAGE = 'view.jpg' #output path

# setup teardown actions
def signal_handler(sig, frame):
  print('cleaning up before exit..')
  camera.stop_preview()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while(True):
  snap(OUT_IMAGE)
  post_file(OUT_IMAGE)
  time.sleep(STREAM_DELAY)
