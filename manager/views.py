from django.shortcuts import render,redirect
from manager.models import Author

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
        writer=Author(name=name,place=place,about=profile,dob=dob,image=profile_pic)
        writer.save()
        return redirect("list_authors")
    return render(request,"add-author.html")

def allAuthors(request):
    malayalam_authors =Author.objects.all() # Getting all data from Author model
    print(malayalam_authors)
    context={"authors":malayalam_authors,"user":"Ebin"}
    return render(request,"list-authors.html",context)

def authorDetail(request,author_id):
    writer=Author.objects.get(id=author_id)
    print(writer)
    return render(request,"author-detail.html",{"author":writer})

def editAuthor(request,writer_id):
    author=Author.objects.get(id=writer_id)
    return render(request,"edit-author.html",{"writer":author})