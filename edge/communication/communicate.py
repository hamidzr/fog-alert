#!/bin/end python

# provides communication between the edge node and the server

from StringIO import StringIO
from PIL import ImageGrab

def send_image():
  content_type = 'image/jpeg'
  headers = {'content-type': content_type}

  screen = ImageGrab.grab()
  img = stringIO()
  screen.save(img, 'JPEG')
  img.seek(0)
  fd = open('screen.jpg', 'wb')
  fd.write(img.getvalue())
  fd.close()
  fin = open('screen.jpg', 'wb')
  files = {'file': ('test.jpg', img, content_type)}
  requests.post('http://localhost/upload', files=files)
