from flask import request, Flask

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test_post():
  print('got a post request', request)
  return "got"

@app.route('/upload', methods=['POST'])
def upload():
  posted_file = request.files['file']
  filename = 'afilename'
  posted_file.save(os.path.join('uploads'), filename)

@app.route('/')
def hello():
  return "Hello World!"

if __name__ == '__main__':
    app.run()
