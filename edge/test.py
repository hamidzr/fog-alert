from picamera import PiCamera
from time import sleep
from PIL import ImageGrab
from StringIO import StringIO

camera = PiCamera()

for i in range(5):
  sleep(5)
  camera.capture('/home/pi/image%s.jpg' % i)
  camera.stop_preview()



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
