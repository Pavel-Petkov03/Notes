from django.urls import path

from djangoProject1.polls.views.add_note import AddNoteView
from djangoProject1.polls.views.delete_note import DeleteView
from djangoProject1.polls.views.details_note import DetailsView
from djangoProject1.polls.views.edit_note import EditNoteView
from djangoProject1.polls.views.home import HomeView
from djangoProject1.polls.views.profile import ProfileView

urlpatterns = [
    path("", HomeView.as_view()),
    path("add", AddNoteView.as_view()),
    path("edit/<int:pk>", EditNoteView.as_view()),
    path("details/<int:pk>", DetailsView.as_view()),
    path("delete/<int:pk>", DeleteView.as_view()),
    path("profile", ProfileView.as_view()),
]
