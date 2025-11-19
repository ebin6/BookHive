from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=70)
    place=models.CharField(max_length=30)
    about=models.TextField()
    image=models.ImageField(upload_to="author") # pillow package must be installed
    dob=models.DateField()

    def __str__(self):
        return self.name
