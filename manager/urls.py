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
    path("list-books",views.AllBooksView.as_view(),name="list_books"),
    path("book-detail/<slug:book_link>",views.BookDetail.as_view(),name="book_detail"),
    path("update-book/<slug:book_slug>",views.UpdateBook.as_view(),name="edit_book"),
    path("delete-book/<slug:slug>",views.DeleteBook.as_view(),name="delete_book"),
    path("books/<slug:slug>/like/",views.bookLike,name="book_like")
]

