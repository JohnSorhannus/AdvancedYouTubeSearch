from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, Template
from django.views.decorators.csrf import csrf_exempt
from django.core import management
from django.core.paginator import Paginator
from pytube import YouTube, extract
from celery import Celery
from .models import *
import time
from search.tasks import analyzevideo
#from .tasks import analyzevideo

# Create your views here.
def home(request):
	return render(request, 'search/home.html')

def searchResults(request):
	start = time.perf_counter()
	query = request.GET
	myargs = {}
	videos = Video.objects.none()

	if query['title']:
		myargs['title__icontains'] = query['title']

	if query['description']:
		myargs['description__icontains'] = query['description']

	if query['user']:
		myargs['user__iexact'] = query['user']

	if query['caption']:
		myargs['captions__icontains'] = query['caption']

	if query['date1'] and query['date2']:
		myargs['upload_date__range'] = [query['date1'], query['date2']]

	print(myargs)

	if myargs:
		videos = Video.objects.filter(**myargs)

	objects = [v for k, v in query.items() if 'object' in k]

	#filter set for each object
	for obj in objects:
		if obj and videos:
			videos = videos.filter(object__name__iexact=obj)
		elif obj and not myargs and not videos:
			videos = Video.objects.filter(object__name__iexact=obj)
		
		if not videos:
			break

	paginator = Paginator(videos, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	end = time.perf_counter()
	print("Search results in " + str((end - start) * 1000) + " seconds")
	print("Number of results: " + str(len(videos)))

	return render(request, 'search/results.html', {'videos': page_obj})

@csrf_exempt
def addVideo(request):
	if request.method == "POST":
		url = request.POST['url']
		is_valid = False
		video_exists = False
		try:
			vid_id = extract.video_id(url)
			video_exists = Video.objects.filter(video_id=vid_id).exists()
			if not video_exists:
				vid = YouTube(url)
				is_valid = True
				analyzevideo.delay(url)
		except:
			pass
		return JsonResponse({'is_valid': is_valid, 'video_exists': video_exists})
