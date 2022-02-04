from django.shortcuts import render, redirect
from django.views import View

from djangoProject1.polls.forms.add_note_form import AddNoteForm
from djangoProject1.polls.models import Note


class EditNoteView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(instance=current_note)
        return render(req, "note-edit.html", {'form': form})

    def post(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(req.POST, instance=current_note)
        form.save()
        return redirect("/")
