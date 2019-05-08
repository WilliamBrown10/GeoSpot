from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


def home(request):
    return render(request, 'userhome/home.html')


def about(request):
    return render(request, 'userhome/about.html', {'title': 'About'})


@login_required
def location(request):
    if not request.user.is_superuser:
       return HttpResponse('In order to access this page you must have SuperUser permissions!')
    else:
    	return render(request, 'userhome/location.html')
