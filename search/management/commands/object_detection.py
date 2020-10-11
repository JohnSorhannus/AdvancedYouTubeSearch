"""
object_detection.py

Contains functions that splices videos into images and detects objects contain within them
"""

import sys
import cv2
import pathlib
import os

#https://stackoverflow.com/a/47632941/7412757
def extract_images(vid_id):
    count = 0
    vidcap = cv2.VideoCapture(str(pathlib.Path(__file__).parent.absolute()) + '/videos/' + vid_id + '.mp4')
    success,image = vidcap.read()
    success = True
    print('Extracting images...')
    while success:
        cv2.imwrite(str(pathlib.Path(__file__).parent.absolute()) + '/screencaps/' + vid_id + '_' + str(count) +  '.jpg', image)     # save frame as JPEG file
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*2000))    # added this line 
        success,image = vidcap.read()
        count = count + 1
    print('Extracted ' + str(count) + ' images')
    os.remove(str(pathlib.Path(__file__).parent.absolute()) + '/videos/' + vid_id + '.mp4')
