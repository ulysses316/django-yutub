from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mail = models.models.EmailField(max_length=60)
    profile_picture = models.ImageField(
        upload_to = "user/pictures",
        blank = True,
        null = True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username