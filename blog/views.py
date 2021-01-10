from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html',{'titles':'Django','link':'http://127.0.0.1:8000'})

# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def expression(request):
    # a=int(request.GET['text1'])
    # b=int(request.GET['text2'])
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+b
    return render(request, 'output.html',{'result':c})