from django.urls import path
from manager import views

urlpatterns=[
    path("",views.managerDashboard,name="dashboard"),
    path("add-author",views.addAuthor,name="create_author"),
    path('all-authors',views.allAuthors,name="list_authors"),
    path("author-detail/<slug:link>",views.authorDetail,name="author_detail"),
    path("edit-author/<slug:link>",views.editAuthor,name="edit_author"),
    path("remove-author/<slug:link>",views.deleteAuthor,name="delete_author"),

    # Books 
    path("add-book",views.addBook,name="add_book"),
    path("list-books",views.AllBooksView.as_view(),name="list_books")
]