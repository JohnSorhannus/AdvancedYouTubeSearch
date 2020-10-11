"""
object_detection.py

Contains functions that splices videos into images and detects objects contain within them
"""

import sys
import cv2
import pathlib

#https://stackoverflow.com/a/47632941/7412757
def extract_images(vid_id):
    count = 0
    vidcap = cv2.VideoCapture('videos/' + vid_id + '.mp4')
    success,image = vidcap.read()
    success = True
    while success:
        cv2.imwrite('screencaps/' + vid_id + '_' + str(count) +  '.jpg', image)     # save frame as JPEG file
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
        success,image = vidcap.read()
        count = count + 1