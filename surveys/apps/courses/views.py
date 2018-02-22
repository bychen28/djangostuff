from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def index(request):
	courses = dict()
	courses['courses'] = Course.objects.all()
	return render(request, 'courses/index.html', courses)
def show(request, ids):
	courses = dict()
	courses['courses'] = Course.objects.get(id = ids)
	return render(request, 'courses/delete.html', courses)
def create(request):
	if request.method == "POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/courses')
		else:
			
			Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
	return redirect('/courses')

def delete(request, ids):
	user = Course.objects.get(id = ids)
	user.delete()
	return redirect('/courses')