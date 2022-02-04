from django.shortcuts import redirect

# Create your views here.
from .models import Note, Profile
from django.shortcuts import render
from django.views import View
from djangoProject1.polls.forms.add_note_form import AddNoteForm
from djangoProject1.polls.forms.add_profile_form import AddProfileForm


class HomeView(View):
    def get(self, req):
        if Profile.objects.all().__len__() == 0:
            Note.objects.all().delete()
            return render(req, "home-no-profile.html", {"form": AddProfileForm()})
        else:
            all_notes = Note.objects.all()
            profile = Profile.objects.get(id=1)
            return render(req, "home-with-profile.html", {"profile": profile, "all_notes": all_notes, })

    def post(self, req):
        print(1)



class AddNoteView(View):
    def get(self, req):
        return render(req, "note-create.html", {"form": AddNoteForm()})

    def post(self, req, **kwargs):
        add_form = AddNoteForm(req.POST)
        add_form.save()
        return redirect("/add")


class EditNoteView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(instance=current_note)
        return render(req, "note-edit.html", {'form': form})

    def post(self, req, pk):
        current_note = Note.objects.get(id=pk)
        form = AddNoteForm(req.POST, instance=current_note)
        form.save()
        redirect("/")


class DetailsView(View):
    def get(self, req, pk):
        current_note = Note.objects.get(id=pk)
        return render(req, "note-details.html", {"note": current_note})


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


class ProfileView(View):
    def get(self, req):
        current_user = Profile.objects.get(id=1)
        notes = Note.objects.all().__len__()
        return render(req, "profile.html", {"user": current_user, "notes": notes})

    def post(self, req):
        Profile.objects.get(id=1).delete()
        Note.objects.all().delete()
        return redirect("/")
