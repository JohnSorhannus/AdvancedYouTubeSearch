"""
analyzevideos.py

Script to be executed that calls functions that analyzes videos. Meant to be executed before running django server for the first time.
"""

import search.management.commands.extract_metadata as emd
import search.management.commands.object_detection as od
from pytube import extract
from django.core.management import BaseCommand
from search.models import *

class Command(BaseCommand):
	"""docstring for Command"""
	def handle(self, **options):
		videos = ['https://www.youtube.com/watch?v=dEcsD_EEnBo&ab_channel=FOX11LosAngeles'
		]

		count = 1
		for video in videos:
			print('Video ' + str(count) + '/' + str(len(videos))) 
			vid_id = extract.video_id(video)
			if not Video.objects.filter(video_id=vid_id).exists():
				emd.download_video(video)
				od.extract_images(vid_id)
				od.detect_objects(vid_id)

			count += 1

