from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=True)
    media = models.FileField(upload_to="videos/media_upload", max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.user.username})'