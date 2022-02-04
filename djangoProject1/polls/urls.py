# •	http://localhost:8000/ - home page
# •	http://localhost:8000/add - add note page
# •	http://localhost:8000/edit/:id - edit note page
# •	http://localhost:8000/delete/:id - delete note page
# •	http://localhost:8000/details/:id - note details page
# •	http://localhost:8000/profile - profile page
from django.urls import path

from djangoProject1.polls.views import HomeView, AddNoteView, EditNoteView, DetailsView, DeleteView

urlpatterns = [
    path("", HomeView.as_view()),
    path("add", AddNoteView.as_view()),
    path("edit/<int:pk>", EditNoteView.as_view()),
    path("details/<int:pk>", DetailsView.as_view()),
    path("delete/<int:pk>", DeleteView.as_view()),
    path("profile", DeleteView.as_view()),
]
