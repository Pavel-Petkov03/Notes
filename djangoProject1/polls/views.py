from django.shortcuts import render, redirect

# Create your views here.
from .models import Note

from django.shortcuts import render
from django.views import View
from .forms import AddNoteForm


class HomeView(View):
    def get(self, req):
        return render(req, "home-no-profile.html")


class AddNoteView(View):
    def get(self, req):
        return render(req, "note-create.html", {"form": AddNoteForm()})

    def post(self, req, **kwargs):
        add_form = AddNoteForm(req.POST)
        if add_form.is_valid():
            image_url = add_form.cleaned_data["image_url"]
            title = add_form.cleaned_data["title"]
            description = add_form.cleaned_data["description"]
            current_note = Note(image_url=image_url, title=title, content=description)
            current_note.save()
            return redirect("/")
        else:
            return redirect("/add")


class EditNoteView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        a = AddNoteForm()
        return render(req, "note-edit.html", {'note': current_note})

    def post(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(req.POST)
        if form.is_valid():
            current_note.image_url = form.cleaned_data["image_url"]
            current_note.content = form.cleaned_data["content"]
            current_note.content = form.cleaned_data["title"]
            current_note.save()
            redirect("/")
        else:
            redirect("/add")


