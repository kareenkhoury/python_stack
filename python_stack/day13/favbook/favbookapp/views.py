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
        user=User.objects.last()
        request.session['user_id']=user.id
    return redirect('/books')


def login(request):
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.filter(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id']=user.id
            return redirect('/books')
    messages.error(request, 'Invalid Credentials')
    return redirect('/')


def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
            'allbooks' : Book.objects.all(),
            'user': User.objects.get(id=request.session['user_id'])
        }
    return render(request,"books.html",context)


def createbook(request):
    errors = Book.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user=User.objects.get(id=request.session['user_id'])
        book=Book.objects.create(title=request.POST['title'],description=request.POST['description'], 
                            uploaded_by=user)
        user.liked_books.add(book)
        return redirect('/books')

def viewbook(request,id):
    user=User.objects.get(id=request.session['user_id'])
    book=Book.objects.get(id=id)
    context={
        'user':user,
        'book':book,
    }
    return render(request, 'view.html',context)

def addfav(request , book_id, user_id):
    book=Book.objects.get(id=book_id)
    user=User.objects.get(id=user_id)
    book.users_who_like.add(user)
    book.save()
    return redirect('/books')

def update(request,book_id):
    errors = Book.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/books/' + str(book_id))
    else:
        book=Book.objects.get(id=book_id)
        book.title=request.POST['title']
        book.description=request.POST['description']
        book.save()
        return redirect('/books')
    
def delete(request, book_id):
    book=Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')


def unfav(request,book_id):
    user_id=request.session['user_id']
    book=Book.objects.get(id=book_id)
    user=User.objects.get(id=user_id)
    book.users_who_like.remove(user)
    book.save()
    return redirect ('/books')


def logout(request):
    del request.session['user_id']
    return redirect('/')