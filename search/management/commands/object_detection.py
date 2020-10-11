"""
object_detection.py

Contains functions that splices videos into images and detects objects contain within them
"""

import sys
import cv2
import pathlib

def extract_images(vid_id):
	count = 0
	vidcap = cv2.VideoCapture(str(pathlib.Path(__file__).parent.absolute()) + '/videos/' + vid_id + '.mp4')
	success, image = vidcap.read()
	success = True
	while success:
		vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
		success, image = vidcap.read()
		cv2.imwrite(str(pathlib.Path(__file__).parent.absolute()) + '/screencaps/' + vid_id + '_' + count + '.jpg')
		count += 1

def extract_images(vid_id):
	count = 0
	vidcap = cv2.VideoCapture('/videos/' + vid_id + '.mp4')
	success, image = vidcap.read()
	success = True
	while success:
		vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))
		success, image = vidcap.read()
		cv2.imwrite('/screencaps/' + vid_id + '_' + str(count) + '.jpg')
		count += 1