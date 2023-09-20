from django.shortcuts import render
from .models import user

def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        new_user = user(first_name=first_name, last_name=last_name, email_address=email, age=age)
        new_user.save()
    context = {
        "all_user":user.objects.all()
    }
    return render(request, "index.html", context)
