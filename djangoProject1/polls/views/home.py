from django.shortcuts import redirect, render
from django.views import View

from djangoProject1.polls.forms.add_profile_form import AddProfileForm
from djangoProject1.polls.models import Profile, Note


class HomeView(View):
    def get(self, req):
        if not Profile.objects.exists():
            Note.objects.all().delete()
            return render(req, "home-no-profile.html", {"form": AddProfileForm()})
        else:
            all_notes = Note.objects.all()
            profile = Profile.objects.all()[0]
            return render(req, "home-with-profile.html", {"profile": profile, "all_notes": all_notes, })

    def post(self, req):
        add_form = AddProfileForm(req.POST)
        add_form.save()
        return redirect("/")
