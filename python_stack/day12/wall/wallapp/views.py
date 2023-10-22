
from django.shortcuts import render,redirect
from . models import *
import bcrypt
from django.contrib import messages

def index(request):
    return render(request ,"index.html")

def registration(request):
    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        hashed=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=fname,last_name=lname,email=email,password=hashed)
        new_user=User.objects.last()
        request.session['user_id']=new_user.id
    return redirect('/wall')


def login(request):
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.filter(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id']=user.id
            return redirect('/wall')
    messages.error(request, 'Invalid Credentials')
    return redirect('/')

def wall(request):
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'allmessages':Message.objects.all().order_by("-created_at"),
        'allcomments':Comment.objects.all()
    }
    return render(request ,"wall.html",context)

def clickpost(request,id):
    user=User.objects.get(id=id)
    Message.objects.create(message=request.POST['message'], user=user)
    request.session['user_id']
    request.session['message']=request.POST['message']
    return redirect("/wall")

def clickcomment(request):
    message=Message.objects.get(id=request.POST['message'])
    user=User.objects.get(id=request.POST['user'])
    Comment.objects.create(comment=request.POST['comment'],message=message, user=user)
    
    return redirect("/wall")


def delete(request,id):
    message=Message.objects.get(id=id)
    message.delete()
    return redirect("/wall")