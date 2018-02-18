from django.shortcuts import render, render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
	return render(request, 'session_words/index.html')

def process(request):
	if request.method == "POST":
		if 'size' not in request.POST:
			size = "none"
		else:
			size = "uppercase"

		if 'color' not in request.POST:
			color = "black"
		else:
			color = request.POST['color']

		data = {
			'word': request.POST['word'],
			'color': color,
			'size': size,
			'time': strftime("%I:%M:%S %p, %B-%d-%Y", gmtime())
		}

		if 'allwords' not in request.session:
			request.session['allwords'] = []

		fuckthis = request.session['allwords']
		fuckthis.append(data)
		request.session['allwords'] = fuckthis

		for i in range(0, len(request.session['allwords'])):
		 	print request.session['allwords'][i]['size']
	return redirect('/session_words')

def clear(request):
	request.session['allwords'] = []
	return redirect('/session_words')