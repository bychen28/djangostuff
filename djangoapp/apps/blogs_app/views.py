from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visitedcopy
def index(request):
	response = "Placeholder to later display all the list of blogs"
	return HttpResponse(response)

def show(request, number):
	response = "placeholder to display blog " + number
	return HttpResponse(response)

def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def edit(request, number):
	response = "placeholder to edit blog " + number
	return HttpResponse(response)

def destroy(request, number):
	return redirect('/')