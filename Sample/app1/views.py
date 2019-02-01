from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<b>Jay Swaminarayan</b>")

# Create your views here.
