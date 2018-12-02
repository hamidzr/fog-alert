#!/bin/env python

"""
publishes detection of a threat to subscribers
"""
import time

def trigger_response():
  print('sending threat response request..')
  time.sleep(0.5)


if __name__ == '__main__':
  trigger_response()
