#!/bin/end python

# provides shots from the camera

from picamera import PiCamera
import argparse
import time

camera = PiCamera()

def prep_camera():
  print('preparing the camera..')
  # camera.resolution = (1024, 768)
  camera.start_preview()
  # camera.shutter_speed = int(400 * 1e+3) # is in micro seconds (type in ms)
  time.sleep(5)
  print('finished preparing the camera')

# captures a frame
def snap(out_path):
  print('taking a pic..')
  camera.capture(out_path)
  print('snapped a pic')

prep_camera()

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("image_path", help="path to the output image file")
  args = parser.parse_args()
  snap(args.image_path)
  camera.stop_preview()
