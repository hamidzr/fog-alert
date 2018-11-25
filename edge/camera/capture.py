#!/bin/end python

# provides shots from the camera

from picamera import PiCamera

camera = PiCamera()

camera.capture('/home/pi/image%s.jpg' % i)
camera.stop_preview()
