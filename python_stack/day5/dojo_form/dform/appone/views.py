from os import name
from django.shortcuts import render, redirect # don't forget to import redirect!
def index(request):
    # this is the route that shows the form
    return render(request,"index.html")
def create_user(request):
    # this is the route that processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    font_from_form = request.POST['font']
    language_from_form = request.POST['language']
    
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form,
        "font_on_template" : font_from_form,
        "language_on_template" :  language_from_form
    }
    return redirect("/result")
def result(request): # this is the route that processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    font_from_form = request.POST['font']
    language_from_form = request.POST['language']
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form,
        "font_on_template" : font_from_form,
        "language_on_template" :  language_from_form
    }
    return render(request,"result.html",context)

 
 