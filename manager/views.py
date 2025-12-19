from django.shortcuts import render,redirect,get_object_or_404
from manager.models import Author,Book,BookLike
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm
from django.views.generic import ListView,UpdateView,DetailView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse
# Create your views here.

@login_required(login_url="signin")
def managerDashboard(request):
    user="Ebin"
    return render(request,"manager-dashboard.html",{"name":user})

@login_required(login_url="signin")
def addAuthor(request):
    if request.method=="POST":
        name=request.POST['author_name']
        dob=request.POST['dob']
        profile=request.POST['about']
        place=request.POST['place']
        profile_pic=request.FILES.get('picture',None)

        writer=Author(name=name,place=place,about=profile,dob=dob,image=profile_pic)
        writer.save()
        messages.success(request,"New author added ")
        return redirect("list_authors")
    return render(request,"add-author.html")


def allAuthors(request):
    malayalam_authors =Author.objects.all() # Getting all data from Author model
    print(malayalam_authors)
    context={"authors":malayalam_authors,"user":"Ebin"}
    return render(request,"list-authors.html",context)

def authorDetail(request,link):
    writer=Author.objects.get(slug=link)
    # books=Book.objects.filter(author=writer)
    books=writer.books.all()
    return render(request,"author-detail.html",{"author":writer,"books":books})

@login_required(login_url="signin")
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
        messages.info(request,"Updated author details")
        return redirect("author_detail",author.slug)
    return render(request,"edit-author.html",{"writer":author})
@login_required(login_url="signin")
def deleteAuthor(request,link):
    writer=Author.objects.get(slug=link)
    writer.delete()
    messages.success(request,"Author deleted ")
    return redirect("list_authors")

@login_required(login_url="signin")
def addBook(request):
    if request.method=="POST":
        my_form=BookForm(request.POST,request.FILES)
        if my_form.is_valid():
            my_form.save()
            messages.success(request,"New Book added")
            return redirect("add_book")
        else:
            print(my_form.errors)
            return redirect("add_book")
    else:
        my_form=BookForm()
    return render(request,"add-book.html",{"form":my_form})

class AllBooksView(ListView):
    template_name="all-books.html"
    queryset=Book.objects.all()
    context_object_name="books"

class BookDetail(DetailView):
    template_name='book-details.html'
    model=Book
    context_object_name="book"
    slug_field="slug"
    slug_url_kwarg="book_link"


class UpdateBook(SuccessMessageMixin,UpdateView):
    template_name="update-book.html"
    form_class=BookForm
    model=Book
    slug_field="slug"
    slug_url_kwarg="book_slug"
    success_url="/manager/list-books"
    success_message="Book details updated"

    def get_success_url(self):
        return reverse("book_detail",kwargs={"book_link":self.object.slug})



class DeleteBook(DeleteView):
    model=Book
    slug_field="slug"
    success_url=reverse_lazy("list_books")



def bookLike(request, slug):
    book = get_object_or_404(Book, slug=slug)
    like, created = BookLike.objects.get_or_create(book=book,user=request.user)

    if not created:
        like.delete()
        messages.info(request, "You unliked this book.")
    else:
        messages.success(request, "You liked this book.")

    return redirect(book.get_absolute_url())
