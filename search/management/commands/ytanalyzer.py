"""
ytanalyzer.py

Contains functions that extract meta data and objects from videos and inserts data into database
"""

from pytube import YouTube
from pytube import extract
from search.models import Video

def download_videos():
	video = YouTube('https://www.youtube.com/watch?v=At3xcj-pTjg&ab_channel=CaseyNeistat')

	entry = Video(title=video.title,
		description=video.description,
		upload_date='2016-12-20',
		user=video.author,
		captions='',
		thumbnail_url=video.thumbnail_url,
		video_url='https://www.youtube.com/watch?v=At3xcj-pTjg&ab_channel=CaseyNeistat',
		length=video.length,
		views=video.views,
		video_id=extract.video_id('https://www.youtube.com/watch?v=At3xcj-pTjg&ab_channel=CaseyNeistat'))

	entry.save()