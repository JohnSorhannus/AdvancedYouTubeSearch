"""
object_detection.py

Contains functions that splices videos into images and detects objects contain within them
"""

from darkflow.net.build import TFNet
from search.models import *
import sys
import cv2
import pathlib
import os
import json

#https://stackoverflow.com/a/47632941/7412757
def extract_images(vid_id):
    count = 0
    abs_path = str(pathlib.Path(__file__).parent.absolute())
    vidcap = cv2.VideoCapture(abs_path + '/videos/' + vid_id + '.mp4')
    success,image = vidcap.read()
    success = True
    print('Extracting images...')
    while success:
        cv2.imwrite(abs_path + '/screencaps/' + vid_id + '_' + str(count) +  '.jpg', image)     # save frame as JPEG file
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*2000))    # added this line 
        success,image = vidcap.read()
        count = count + 1
    print('Extracted ' + str(count) + ' images')
    os.remove(abs_path + '/videos/' + vid_id + '.mp4') #delete video

def detect_objects(vid_id):
	abs_path = str(pathlib.Path(__file__).parent.absolute())
	darkflow_path = 'darkflow'
	options = {"model": darkflow_path + "/cfg/yolo.cfg", "load": darkflow_path + "/bin/yolo.weights", "threshold": 0.25}

	tfnet = TFNet(options)

	screencap_path = abs_path + '/screencaps/'
	images = [x for x in os.listdir(screencap_path) if x.endswith('.jpg')]

	count = 1
	for img in images:
		print('Extracting objects from frame ' + str(count) + '/' + str(len(images)))
		imgcv = cv2.imread(screencap_path + img)
		result = tfnet.return_predict(imgcv)
		for dict_ in result:
			obj = dict_['label']
			try:
				#check if object already exists in db
				obj_db = Object.objects.get(name=obj)
			except:
				#object does not exist yet
				obj_db = Object(name=obj)
				obj_db.save()
			finally:
				#objet is in database, whether it was already there or just created, so associate object with video
				video = Video.objects.get(video_id=vid_id)
				obj_db.videos.add(video)
		os.remove(screencap_path + img)
		count += 1
