from django.db import models
from django.utils.text import slugify
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=70)
    place=models.CharField(max_length=30)
    about=models.TextField()
    image=models.ImageField(upload_to="author") # pillow package must be installed
    dob=models.DateField()
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args,**kwargs)
    

class Category(models.Model):
    category=models.CharField(max_length=30,unique=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.category
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.category)
        return super().save(*args,**kwargs)
    
