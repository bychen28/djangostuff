from django.shortcuts import render, render, HttpResponse, redirect

def index(request):
	return render(request, 'survey_form/index.html')

def process(request):
	if request.method == "POST":
		if 'count' not in request.session:
			request.session['count'] = 0
		request.session['count'] += 1
		request.session['name'] = request.POST['name']
		request.session['loc'] = request.POST['loc']
		request.session['lang'] = request.POST['lang']
		request.session['com'] = request.POST['com']
	return redirect('/result')

def result(request):
	return render(request, 'survey_form/info.html')

def back(request):
	return redirect('/')