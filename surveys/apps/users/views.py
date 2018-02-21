from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
	users = dict()
	users['users'] = User.objects.all()
	return render(request, 'users/index.html', users)

def show(request, ids):
	users = dict()
	users['users'] = User.objects.get(id = ids)
	return render(request, 'users/show.html', users)

def new(request):
	return render(request, 'users/newuser.html')

def create(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/users/new')
		else:
			User.objects.create(name = request.POST['name'], email = request.POST['email'])
	return redirect('/users')

def edit(request, ids):
	users = dict()
	users['users'] = User.objects.get(id = ids)
	return render(request, 'users/edituser.html', users)

def update(request, ids):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/users/' + ids + '/edit')
		else:
			u = User.objects.get(id = ids)
			u.name = request.POST['name']
			u.email = request.POST['email']
			u.save()
	return redirect('/users')

def delete(request, ids):
	user = User.objects.get(id = ids)
	user.delete()
	return redirect('/users')

