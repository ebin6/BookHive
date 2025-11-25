from django.shortcuts import render,redirect
from manager.models import Author
from django.utils.text import slugify

# Create your views here.
def managerDashboard(request):
    user="Ebin"
    return render(request,"manager-dashboard.html",{"name":user})

def addAuthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        profile_pic=request.FILES['picture']
        link=slugify(name)
        writer=Author(name=name,place=place,about=profile,dob=dob,image=profile_pic,slug=link)
        writer.save()
        return redirect("list_authors")
    return render(request,"add-author.html")

def allAuthors(request):
    malayalam_authors =Author.objects.all() # Getting all data from Author model
    print(malayalam_authors)
    context={"authors":malayalam_authors,"user":"Ebin"}
    return render(request,"list-authors.html",context)

def authorDetail(request,link):
    writer=Author.objects.get(slug=link)
    print(writer)
    return render(request,"author-detail.html",{"author":writer})

def editAuthor(request,link):
    author=Author.objects.get(slug=link)
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        """
        get method prevents from raising MultiValuDictKey Error 
        So even if no value has been given in input field it dose not raise error
        """
        profile_pic=request.FILES.get('picture') 
        author.name=name
        author.dob=dob
        author.place=place
        author.about=profile
        # Check if profile pic value is None 
        # if profile_pic is None it means user has not uploaded new image
        if profile_pic:
            author.image=profile_pic
        author.save()
        return redirect("author_detail",author.slug)
    return render(request,"edit-author.html",{"writer":author})

def deleteAuthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    return redirect("list_authors")