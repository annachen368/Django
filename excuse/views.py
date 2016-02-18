from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	excuses = [
		"Hello my name is Anna",
		"I'd like to join django",
		"It works on my machine",
		"Not today, thanks",
	]

	return HttpResponse(excuses[0])
