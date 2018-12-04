#!/bin/env python

"""
given an image file detect intrusion.
at the bare minimum should support linux cli with a true or false response.
true: intrusion detected, false: all safe
it could be extended to return the identified class among many w/ confidence scores and more
"""

import random
import time


# gets an image path
def has_intruder(image_path):
  with open(image_path, 'rb') as image:
    print('doing intrusion detection magic..')
    time.sleep(2)
    return random.choice([True, False])


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("image_path", help="path to the image file for detection")
  args = parser.parse_args()

  print('intruder') if has_intruder(args.image_path) else print('safe')
