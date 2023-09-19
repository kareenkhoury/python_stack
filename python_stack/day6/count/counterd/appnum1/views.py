from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if request.method == 'POST':
        if 'add2' in request.POST:
            request.session['count'] += 2
        elif 'reset' in request.POST:
            request.session['count'] = 0
        else:
            request.session['count'] += 1
        return redirect('index')
    return render(request, 'index.html', {'count': request.session['count']})

def reset(request):
    request.session['count'] = 0
    return redirect('index')
