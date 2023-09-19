
import random
from django.shortcuts import render, redirect 

def index(request):    
    return render(request, 'index.html')


def process_money(request):
    if request.method == 'POST':
        if request.POST['place'] == 'farm':
            gold = random.randrange(10, 21)
            gold =request.session['gold']
            request.session['activities'] = gold
        elif request.POST['place'] == 'cave':
            gold = random.randrange(10, 21)
            gold =request.session['gold']
            request.session['activities'] = gold
        elif request.POST['place'] == 'house':
            gold = random.randrange(10, 21)
            gold =request.session['gold']
            request.session['activities'] = gold
        elif request.POST['place'] == 'quest':
            gold = random.randrange(0, 51)
            gold =request.session['gold']
            request.session['activities'] = gold
               

    return redirect('/')