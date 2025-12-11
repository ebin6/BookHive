from django.db import models
from django.utils.text import slugify
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("author_detail",kwargs={"link":self.slug})
    
    def save(self,*args,**kwargs):
        if not self.slug:
            count=1
            slug_url=slugify(self.name)
            while Author.objects.filter(slug=slug_url).exists():
                slug_url=slugify(f"{self.name} {count}")
                count+=1
                
            self.slug=slug_url   
                

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
    

class Book(models.Model):
    book=models.CharField(max_length=60,unique=True)
    about=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    author=models.ForeignKey(Author,on_delete=models.PROTECT)
    publish_date=models.DateField()
    date=models.DateField(auto_now_add=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to="books",default="books/default_cover_page.png")

    def __str__(self):
        return self.book
    
    def get_absolute_url(self):
        return reverse("book_detail",kwargs={"book_link":self.slug})
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.book)
        return super().save(*args,*kwargs)
