"""
analyzevideos.py

Script to be executed that calls functions that analyzes videos. Meant to be executed before running django server for the first time.
"""

import search.management.commands.extract_metadata as emd
import search.management.commands.object_detection as od
from django.core.management import BaseCommand

class Command(BaseCommand):
	"""docstring for Command"""
	def handle(self, **options):
		videos = ['https://www.youtube.com/watch?v=dbdYRc5Cc7Y&ab_channel=RAY%21']

		for video in videos:
			vid_id = emd.download_video(video)
			od.extract_images(vid_id)

