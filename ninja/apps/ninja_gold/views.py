from django.shortcuts import render, render, HttpResponse, redirect
import random
def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	return render(request, 'ninja_gold/index.html')

def process(request):
	if request.method == "POST":
		if 'gamelog' not in request.session:
			request.session['gamelog'] = []
		if request.POST['building'] == 'farm':
			request.session['prize'] = random.randrange(10, 21)
			gamelog = request.session['gamelog']
			gamelog.append("Earned " + str(request.session['prize']) + "gold from the farm!")
		elif request.POST['building'] == 'cave':
			request.session['prize'] = random.randrange(5,11)
			gamelog = request.session['gamelog']
			gamelog.append("Earned " + str(request.session['prize']) + "gold from the cave!")
		elif request.POST['building'] == 'house':
			request.session['prize'] = random.randrange(2,6)
			gamelog = request.session['gamelog']
			gamelog.append("Earned " + str(request.session['prize']) + "gold from the house!")
		else: 
			random_number = 0
			if random.random() < 0.5:
				random_number = -1
			else:
				random_number = 1

			request.session['prize'] = (random.randrange(0, 51) * random_number)
			if request.session['prize'] < 0:
				gamelog = request.session['gamelog']
				gamelog.append("Lost " + str(request.session['prize']) + " gold from the casino!")
			else:
				gamelog = request.session['gamelog']
				gamelog.append("Earned " + str(request.session['prize']) + " gold from the casino!")
		request.session['gold'] += request.session['prize']
		request.session['gamelog'] = gamelog
		return redirect('/')
