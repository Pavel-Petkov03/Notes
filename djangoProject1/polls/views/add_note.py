from django.shortcuts import render, redirect
from django.views import View

from djangoProject1.polls.forms.add_note_form import AddNoteForm


class AddNoteView(View):
    def get(self, req):
        return render(req, "note-create.html", {"form": AddNoteForm()})

    def post(self, req, **kwargs):
        add_form = AddNoteForm(req.POST)
        add_form.save()
        return redirect("/add")
