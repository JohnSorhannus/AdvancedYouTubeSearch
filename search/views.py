from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	return render(request, 'search/home.html')

def searchResults(request):
	query = request.GET
	myargs = {}

	if query['title']:
		myargs['title__icontains'] = query['title']

	if query['user']:
		myargs['user__iexact'] = query['user']

	if query['object']:
		myargs['object__name__iexact'] = query['object']

	if query['caption']:
		myargs['captions__icontains'] = query['caption']

	if query['date1'] and query['date2']:
		myargs['upload_date__range'] = [query['date1'], query['date2']]

	videos = Video.objects.filter(**myargs)
	return render(request, 'search/results.html', {'videos': videos})