"""
analyzevideos.py

Script to be executed that calls functions that analyzes videos. Meant to be executed before running django server for the first time.
"""

import search.management.commands.extract_metadata as emd
from django.core.management import BaseCommand

class Command(BaseCommand):
	"""docstring for Command"""
	def handle(self, **options):
		emd.download_videos()
