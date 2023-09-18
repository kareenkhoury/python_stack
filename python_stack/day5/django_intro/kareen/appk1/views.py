

from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse
def root(request):
 return redirect("/blogs")
def index(request):
    return JsonResponse({"message":"placeholder to later display a list of all blogs"})
def new(request):
    return JsonResponse({"message": "placeholder to display a new form to create a new blog"})
def create(request):
 return redirect("/")
def show(request, number ):
   return JsonResponse({"message":"placeholder to display blog number: {number}"})
def edit(request, number ):
   return JsonResponse({"message":"placeholder to edit blog {number}"})
def destroy(request, number ):
 return redirect("/blogs")
def redirected_method(request):
    return JsonResponse({"title": "my first blog", "content": "loren,judseselo kiuuj e"})
