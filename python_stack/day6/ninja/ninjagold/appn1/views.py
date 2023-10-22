import random
from django.shortcuts import render, redirect 

def index(request):
    if 'gold'not in request.session:
        request.session['gold'] = 0
    if 'logs' not in request.session:
        request.session['logs'] = []
    print(len(request.session['logs']))
    print(request.session['gold'])
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'POST':
        if request.POST['place'] == 'farm':
            number = random.randrange(10, 20)
            request.session['gold'] += number
            request.session['number'] = number
        elif request.POST['place'] == 'cave':
            number = random.randrange(10, 20)
            request.session['gold'] += number
            request.session['number'] = number
        elif request.POST['place'] == 'house':
            number = random.randrange(10, 20)
            request.session['gold'] += number
            request.session['number'] = number
        elif request.POST['place'] == 'quest':
            number = random.randrange(-50, 50)
            request.session['number'] = number
            request.session['gold'] += number
        request.session['logs'].append(f"<p style='color:{'green' if request.session['number'] >= 0 else 'red'}'>You entered a {request.POST['place']} and earned {request.session['number']}.</p>") 
    return redirect('/')