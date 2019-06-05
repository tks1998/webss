from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    var = {
        'sanpham' : 'anc'
    }
    return render(request, 'pages/pages1.html',var)
def page2(request, id):
    return render(request, 'pages/pages2.html')
def process(request):
    x = request.POST["chuoi"]
    return HttpResponse(x)