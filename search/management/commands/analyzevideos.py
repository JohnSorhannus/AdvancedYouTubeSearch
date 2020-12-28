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
	def add_arguments(self, parser):
		parser.add_argument('url', type=str, nargs='+', help='URL of video to be added to the Advanced YouTube Search library.')

	"""docstring for Command"""
	def handle(self, **kwargs):
		videos = kwargs['url']
		count = 1
		for video in videos:
			print('Video ' + str(count) + '/' + str(len(videos))) 
			vid_id = extract.video_id(video) # if not a yt url, will fail here
			if not Video.objects.filter(video_id=vid_id).exists():
				emd.download_video(video)
				screeencap_path = od.extract_images(vid_id)
				od.detect_objects(vid_id, screeencap_path)

			count += 1

