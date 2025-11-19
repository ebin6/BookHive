from django.shortcuts import render
from manager.models import Author

# Create your views here.
def managerDashboard(request):
    user="Ebin"
    return render(request,"manager-dashboard.html",{"name":user})

def addAuthor(request):
    return render(request,"add-author.html")

def allAuthors(request):
    malayalam_authors =Author.objects.all() # Getting all data from Author model
    print(malayalam_authors)
    context={"authors":malayalam_authors,"user":"Ebin"}
    return render(request,"list-authors.html",context)

def authorDetail(request):
    writer=Author.objects.get(id=1)
    print(writer)
    return render(request,"author-detail.html",{"author":writer})