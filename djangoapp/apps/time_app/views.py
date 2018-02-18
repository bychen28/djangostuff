from django.shortcuts import render, render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
	data = {
	'date': strftime("%b %d %Y", gmtime()),
	'time': strftime("%H:%M %p", gmtime())
	}
	print data['time']
	return render(request, 'time_app/index.html', data)
# Create your views here.
