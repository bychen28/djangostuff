from django.shortcuts import render, render, HttpResponse, redirect

def index(request):
	return render(request, 'amadon/index.html')

def buy(request):
	if request.method == "POST":
		price = 0
		if 'totalspent' not in request.session:
			request.session['totalspent'] = 0
		if 'totalitems' not in request.session:
			request.session['totalitems'] = 0
		if 'charge' not in request.session:
			request.session['charge'] = 0

		if request.POST['product'] == "shirt":
			price = 19.99
		elif request.POST['product'] == "sweater":
			price = 29.99
		elif request.POST['product'] == "cup":
			price = 4.99
		else:
			price = 49.99

		request.session['charge'] = price * int(request.POST['quantity'])
		request.session['totalitems'] += int(request.POST['quantity'])
		request.session['totalspent'] += int(request.session['charge'])
		
	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon/checkout.html')
