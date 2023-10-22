from django.shortcuts import render, HttpResponse ,redirect
from .models import shows  # Change the model name to 'shows'

def index(request):

    context = {
        "show": shows.objects.all,
    }
    return render(request, "index.html", context)
def display(request, id):
    context = {
        "shows": shows.objects.get(id=id)
    }
    return render(request, "display.html", context)


def edit(request, id):
    context = {
        'shows': shows.objects.get(id=id),
    }
    return render(request, "edit.html", context)


def update(request, id):
    errors = shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/<id>/edit')
    else:
        show = shows.objects.get(id=id)
        show.title = request.POST['title']
        show.Network = request.POST['network']
        show.release_date = request.POST['releasedate']
        show.description = request.POST['description']
        show.save()
    return redirect('/shows/'+str(id))


def delete(request, id):
    shows.objects.get(id=id).delete,
    return redirect('/shows')
def addshow(request):
    return render(request, "addshow.html")
def submitshow(request):
    errors = shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('shows/new')
    else:
        shows.objects.create(
            title=request.POST['title'], Network=request.POST['network'],
            release_date=request.POST['releasedate'], description=request.POST['description'])
        id = shows.objects.last().id
    return redirect('/shows/'+str(id))