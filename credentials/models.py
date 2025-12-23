from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES=(
        ("manager","Manager"),
        ("user","User")
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profile/",default="profile/default_user_image.jpg")
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="user")

    def __str__(self):
        return str(self.user.username)