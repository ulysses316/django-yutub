from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
    
@login_required
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        fileMedia = request.POST.get('fileMedia')
        user = request.user
        video = Video(title=title, description=description, user=user, media=fileMedia)
        video.save()
        return redirect('/')
    return render(request, "templatesBase/upload.html")