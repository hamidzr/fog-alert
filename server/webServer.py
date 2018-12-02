from flask import request, Flask
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
  posted_file.save(UPLOAD_DIR + '/' + sanitize_name(posted_file))

  return 'file saved.'

@app.route('/')
def hello():
  return "Hello World!"

if __name__ == '__main__':
  app.run(port=config['DEFAULT'].get('PORT', 5000),
          debug=config['DEFAULT'].get('DEBUG', True))
