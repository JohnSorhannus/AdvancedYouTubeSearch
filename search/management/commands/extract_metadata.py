"""
extract_metadata.py

Contains functions that extract meta data and objects from videos and inserts data into database
"""

from pytube import YouTube
from pytube import extract
from search.models import Video
import xml.etree.ElementTree as ET
import re
import html
import pathlib

def download_video(url):
	video = YouTube(url)

	try:
		xml_captions = video.captions['en'].xml_captions
		str_captions = extract_captions(xml_captions)
	except:
		str_captions = ''

	vid_id = extract.video_id(url)

	print('Downloading video...')
	videos_path = str(pathlib.Path(__file__).parent.absolute()) + "/videos"
	video.streams.filter(file_extension='mp4').order_by('resolution').desc().first().download(videos_path, vid_id)

	entry = Video(title=video.title,
		description=video.description,
		upload_date=extract_upload_date(video),
		user=video.author,
		captions=str_captions,
		thumbnail_url=video.thumbnail_url,
		video_url=url,
		length=video.length,
		views=video.views,
		video_id=vid_id)

	entry.save()

	print('Video saved to database')

	return vid_id

#pass in xml of captions, converts to string
def extract_captions(xml):
	root = ET.fromstring(xml)
	caption = ''

	for s in root.iter('text'):
		sen = s.text
		matches = re.findall(r"&(?:[a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", sen)
		for item in matches:
			sen = re.sub(item, html.unescape(item), sen)
		caption += sen + ' '

	return caption

#function to extract upload date
def extract_upload_date(video):
	match = re.search(r"(?<=itemprop=\"datePublished\" content=\")\d{4}-\d{2}-\d{2}", video.watch_html)
	return match.group(0)
