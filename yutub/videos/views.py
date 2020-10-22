from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "templatesBase/index.html")

def video(request):
    return render(request, "templatesBase/video.html")

def info(request):
    return HttpResponse("Info")
    
def upload(request):
    return HttpResponse("Upload")