from AdvancedYouTubeSearch.celery import app
from django.core import management

@app.task
def analyzevideo(url):
	management.call_command('analyzevideos', url)
