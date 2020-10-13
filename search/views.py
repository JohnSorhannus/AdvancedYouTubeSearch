from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	return render(request, 'search/home.html')

def searchResults(request):
	videos = Video.objects.all()
	return render(request, 'search/results.html', {'videos': videos})