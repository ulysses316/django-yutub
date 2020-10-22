from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
# Create your views here.

def index(request):
    all_videos = Video.objects.all()
    context = {
        'all_videos': all_videos,
    }
    return render(request, "templatesBase/index.html", context)

def video(request,video_id):
    video_media = Video.objects.filter(id=video_id)
    all_videos = Video.objects.all()
    context = {
        'video_principal': video_media,
        'all_videos': all_videos,
    }
    print (video_media)
    return render(request, "templatesBase/video.html", context)

def info(request):
    return HttpResponse("Info")
    
def upload(request):
    return HttpResponse("Upload")