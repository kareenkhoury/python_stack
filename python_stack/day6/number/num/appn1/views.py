from django.shortcuts import render, redirect
from django.http import JsonResponse
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
       
    return render(request, 'index.html')



def check_guess(request):
    if request.method == 'POST':
       # guess  = {
    	#"guess" : guess,
  #  }
      #  number = request.session['number']
        guess = int(request.POST.get('guess'))
        number = request.session.get('number')
        if guess < number:
            response_data = {'message': 'Too low! Try again.'}
        elif guess > number:
            response_data = {'message': 'Too high! Try again.'}
        else:
            del request.session['number']  # Clear the secret number
            response_data = {
                'message': f'Congratulations! You guessed the number ({number}) '
            }
        return JsonResponse(response_data)
    
    

       

     
