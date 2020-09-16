from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'search/home.html')

def searchResults(request):
	return render(request, 'search/results.html')