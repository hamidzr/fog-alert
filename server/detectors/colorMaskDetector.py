#!/bin/env python
# color based threat detection mechanism

import cv2
import numpy as np


# OPT avoid rereading the image from fs

def pixel_count(image_path):
  img = cv2.imread(image_path)
  return int(img.size / 3)

def color_count(image_path, minBgr, maxBgr):
  img = cv2.imread(image_path)
  dst = cv2.inRange(img, minBgr, maxBgr)
  color_count = cv2.countNonZero(dst)
  return color_count

def red_count(image_path):
  RED_MIN = np.array([0, 0, 200], np.uint8)
  RED_MAX = np.array([50, 50, 255], np.uint8)
  return color_count(image_path, RED_MIN, RED_MAX)

def blue_count(image_path):
  BLUE_MIN = np.array([150, 0, 0], np.uint8)
  BLUE_MAX = np.array([255, 50, 50], np.uint8)
  return color_count(image_path, BLUE_MIN, BLUE_MAX)

def has_intruder(image_path):
  return red_count(image_path) / float(pixel_count(image_path)) > 0.3


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("image_path", help="path to the image file for detection")
  args = parser.parse_args()

  print('total', pixel_count(args.image_path))
  print('red', red_count(args.image_path))
  print('blue', blue_count(args.image_path))
  # print(f'The number of total pixels is: NONE, blue pixels: {blue_count(args.image_path)}'))

