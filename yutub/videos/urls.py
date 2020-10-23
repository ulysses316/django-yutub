from django.urls import path
from . import views

urlpatterns = [
    path('watch/<int:video_id>', views.video, name='videos'), # Llave individual de cada video
    path('upload', views.upload, name='upload'), # Subir un video
]