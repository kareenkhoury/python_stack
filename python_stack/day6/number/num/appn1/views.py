from django.shortcuts import render, redirect

from django.http import JsonResponse
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    print(f"number==> {request.session['number']}")    
    return render(request, 'index.html')

def check_guess(request):
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        number = request.session.get('number')
        print(f"guess==> {guess}", f"number==> {number}")
        if(guess > number ):
            request.session['result'] = "<div style='width:200px; height:200px; text-align:center; background-color:red;'> too heigh</div>"
        elif guess < number:
            request.session['result'] = "<div style='width:200px; height:200px; text-align:center; background-color:red;'> too low</div>"
        elif guess == number:
            request.session['result'] = f"<div style='width:200px; height:200px; text-align:center; background-color:green;'> <b>{guess} was the number</b></div>"
        del request.session['number']  # Clear the secret number
    return redirect('/')