"""
ytanalyzer.py

Contains functions that extract meta data and objects from videos and inserts data into database
"""

from pytube import YouTube
from pytube import extract
from search.models import Video
import xml.etree.ElementTree as ET
import re
import html

def download_videos():
	video = YouTube('https://www.youtube.com/watch?v=DyUrqZBs2XA&ab_channel=CaseyNeistat')

	try:
		xml_captions = video.captions['en'].xml_captions
		str_captions = extract_captions(xml_captions)
	except:
		str_captions = ''

	entry = Video(title=video.title,
		description=video.description,
		upload_date='2016-12-21',
		user=video.author,
		captions=str_captions,
		thumbnail_url=video.thumbnail_url,
		video_url='https://www.youtube.com/watch?v=DyUrqZBs2XA&ab_channel=CaseyNeistat',
		length=video.length,
		views=video.views,
		video_id=extract.video_id('https://www.youtube.com/watch?v=DyUrqZBs2XA&ab_channel=CaseyNeistat'))

	entry.save()

def extract_captions(xml):
	root = ET.fromstring(xml)
	caption = ''

	for s in root.iter('text'):
		sen = s.text
		print(sen)
		matches = re.findall("&(?:[a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", sen)
		for item in matches:
			sen = re.sub(item, html.unescape(item), sen)
		caption += sen + ' '

	return caption
