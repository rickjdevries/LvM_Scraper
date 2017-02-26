from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
    
from django.shortcuts import render

def index(request):
	show_text = "Soon this will be the Event Scraper page!!"
	return render(request,'eventscraper/events.html')