from django.shortcuts import render
from django.views import View

from djangoProject1.polls.models import Note


class DetailsView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        return render(req, "note-details.html", {"note": current_note})