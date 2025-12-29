from django.urls import path
from manager import views

urlpatterns=[
    path("",views.managerDashboard,name="dashboard"),
    path("add-author",views.addAuthor,name="create_author"),

    
    path("edit-author/<slug:link>",views.editAuthor,name="edit_author"),
    path("remove-author/<slug:link>",views.deleteAuthor,name="delete_author"),

    # Books 
    path("add-book",views.addBook,name="add_book"),
  
    path("update-book/<slug:book_slug>",views.UpdateBook.as_view(),name="edit_book"),
    path("delete-book/<slug:slug>",views.DeleteBook.as_view(),name="delete_book"),

]

