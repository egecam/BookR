from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(req):
    name = req.GET['name'] or "World"
    return render(req, 'index.html', {'name': name})


def search(req):
    return HttpResponse("Hello Django")
