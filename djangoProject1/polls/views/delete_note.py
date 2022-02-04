from django.shortcuts import render, redirect
from django.views import View

from djangoProject1.polls.forms.add_note_form import AddNoteForm
from djangoProject1.polls.models import Note


class DeleteView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(instance=current_note)
        form.disable_fields()
        return render(req, "note-delete.html", {"form": form})

    def post(self, req, pk):
        current_note = Note.objects.get(id=pk)
        current_note.delete()
        return redirect("/")
