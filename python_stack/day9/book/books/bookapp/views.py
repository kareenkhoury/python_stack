from turtle import title
from django.shortcuts import render
from .models import books

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        new_book = books( title=title, desc=desc)
        new_book.save()
    context = {
        "books":books.objects.all()
    }
    return render(request, "index.html", context)
def bookview(request, book_id):
    book_queryset = books.objects.filter(id=book_id)

    if book_queryset.exists():
        book = book_queryset.first() 
        context = {
            "book": book
        }
        return render(request, "bookview.html", context)
def addAuthors(request):
  return render(request,"addauthors.html")

def viewAuthor(request,author_id):
   author_queryset = books.objects.filter(id=author_id)
   if  author_queryset.exists():
        author =  author_queryset.first() 
        context = {
            "auth": author
        }
   return render(request,"viewauthors.html")
