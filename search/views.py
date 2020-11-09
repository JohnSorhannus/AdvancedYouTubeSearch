from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import time

# Create your views here.

def home(request):
	return render(request, 'search/home.html')

def searchResults(request):
	start = time.perf_counter()
	query = request.GET
	myargs = {}
	videos = ''

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

	end = time.perf_counter()
	print("Search results in " + str((end - start) * 1000) + " seconds")
	print("Number of results: " + str(len(videos)))

	return render(request, 'search/results.html', {'videos': videos})