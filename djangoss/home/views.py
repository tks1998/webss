from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/pages1.html')
def page2(request, id):
    return render(request, 'pages/pages2.html')
