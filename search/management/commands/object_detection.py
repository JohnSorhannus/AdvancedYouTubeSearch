"""
object_detection.py

Contains functions that splices videos into images and detects objects contain within them
"""

from darkflow.net.build import TFNet
from search.models import *
import sys
import cv2
from pathlib import Path
import json

#https://stackoverflow.com/a/47632941/7412757
def extract_images(vid_id):
    count = 0
    abs_path = Path(__file__).resolve().parent.parent
    video_path = abs_path.joinpath('videos', vid_id + '.mp4')
    vidcap = cv2.VideoCapture(str(video_path))

    success,image = vidcap.read()
    success = True
    print('Extracting images from [' + vid_id + ']...')
    screencap_path = abs_path.joinpath('screencaps', vid_id)
    screencap_path.mkdir(parents=True, exist_ok=True)
    while success:
        cv2.imwrite(str(screencap_path.joinpath(vid_id + '_' + str(count) +  '.jpg')), image)     # save frame as JPEG file
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*2000))    # get frame every 2 seconds
        success,image = vidcap.read()
        count = count + 1
    print('Extracted ' + str(count) + ' images')
    video_path.unlink() #delete video
    return screencap_path

def detect_objects(vid_id, screencap_path):
	darkflow_path = 'darkflow'
	options = {"model": darkflow_path + "/cfg/yolo.cfg", "load": darkflow_path + "/bin/yolo.weights", "threshold": 0.25}

	tfnet = TFNet(options) #neural network library for object detection
	images = [x for x in screencap_path.glob('*.jpg')]

	count = 1
	for img in images:
		print('Extracting objects from frame ' + str(count) + '/' + str(len(images)) + ' for [' + vid_id + ']')
		img_path = screencap_path.joinpath(img)
		imgcv = cv2.imread(str(img_path))
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
		img_path.unlink()
		count += 1
	screencap_path.rmdir()
