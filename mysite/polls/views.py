from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, people this is the index page")