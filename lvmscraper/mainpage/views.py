from django.shortcuts import render

def index(request):
	show_text = "Soon this will be the main page!!"
	return render(request,'mainpage/mainpage.html', {'text': show_text})