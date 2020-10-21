from django.db import models
from users.models import User
# Create your models here.

class Video(models.Model):
    title = models.models.CharField(max_length=30, null=False, blank=False)
    date = models.models.DateField(auto_now=False, auto_now_add=True)
    media = models.models.FileField(upload_to="videos/media_upload", max_length=100)
    description = models.models.TextField(blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)