#!/bin/end python

# provides communication between the edge node and the server

import requests
import os, sys
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

SERVER_URL = config['DEFAULT']['SERVER_URL']

def post_file(file_path):
  filename = os.path.basename(file_path)

  multipart_form_data = {
    'file': (filename, open(file_path, 'rb'))
  }

  response = requests.post(SERVER_URL, files=multipart_form_data)

  # keys = [key for key in response]
  # print(keys)
  print(response.status_code)

if __name__ == '__main__':
  post_file(sys.argv[1])
