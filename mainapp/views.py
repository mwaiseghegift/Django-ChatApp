from django.shortcuts import render

# Create your views here.


def HomePage(request, *args, **kwargs):
    return render(request, 'index.html', {})