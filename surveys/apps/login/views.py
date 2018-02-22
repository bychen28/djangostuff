from django.shortcuts import render, redirect
from .models import Uzer
from django.contrib import messages

def index(request):
	return render(request, 'login/index.html')

def create(request):
	if request.method == "POST":
		Uzer.objects.create(fname = request.POST['fname'], lname = request.POST['lname'],
			email= request.POST['email'], pword = request.POST['pword'])
		print Uzer.objects.all()
	return redirect('/login')