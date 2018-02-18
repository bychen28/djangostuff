from django.shortcuts import render, render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

def index(request):
	if 'count' not in request.session:
		request.session['count'] = 1
	request.session['rndmwrd'] = get_random_string(length = 14)
	return render(request, 'random_word/index.html')

def generate(request):
	request.session['count'] += 1
	return redirect('/random_word')

def reset(request):
	request.session.clear()
	return redirect('/random_word')