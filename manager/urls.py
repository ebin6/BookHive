from django.urls import path
from manager import views

urlpatterns=[
    path("",views.managerDashboard,name="dashboard"),
    path("add-author",views.addAuthor,name="create_author"),
    path('all-authors',views.allAuthors,name="list_authors"),
    path("author-detail/<int:author_id>",views.authorDetail,name="author_detail"),
    path("edit-author/<int:writer_id>",views.editAuthor,name="edit_author"),
    path("remove-author/<int:author_id>",views.deleteAuthor,name="delete_author")
]