from django.shortcuts import render, redirect
from .models import dojo, ninja

def index(request):
    if request.method == 'POST':
       
        if 'add_dojo' in request.POST:
            name = request.POST['name']
            city = request.POST['city']
            state = request.POST['state']
            new_dojo = dojo(name=name, city=city, state=state)
            new_dojo.save()
        
       
        elif 'add_ninja' in request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            dojo_id = request.POST['dn']
            selected_dojo = dojo.objects.get(id=dojo_id) 
            new_ninja = ninja(first_name=first_name, last_name=last_name, dojo_id=selected_dojo)
            new_ninja.save()
        elif 'delete_dojo' in request.POST:
            dojo_to_delete = dojo.objects.get(id=dojo)
            dojo_to_delete.delete()

    context = {
        "dojos": dojo.objects.all(),
    }
    
    return render(request, "index.html", context)
