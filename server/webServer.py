from flask import request, Flask
import detectors.colorMaskDetector as colorMaskDetector
from communicate import trigger_response
import configparser
import os

# load configuration in
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

UPLOAD_DIR='./uploads'

def sanitize_name(uploaded_file):
  # TODO SEC actually sanitize
  return uploaded_file.filename

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test_post():
  print('got a post request', request)
  return "got"

@app.route('/upload', methods=['POST'])
def upload():

  print(request.files)
  if 'file' not in request.files:
    return '"file" field does not exist.'

  posted_file = request.files['file']
  file_name = sanitize_name(posted_file)
  save_path = UPLOAD_DIR + '/' + file_name
  posted_file.save(save_path)
  detected = colorMaskDetector.has_intruder(save_path)
  # TODO trigger w/o blocking or trigger response elsewhere
  print('threat:', detected)
  if detected: trigger_response()
  return str(detected)

@app.route('/')
def hello():
  return "Hello World!"

if __name__ == '__main__':
  app.run(port=config['DEFAULT'].get('PORT', 5000),
          debug=config['DEFAULT'].get('DEBUG', True),
         host= '0.0.0.0')
