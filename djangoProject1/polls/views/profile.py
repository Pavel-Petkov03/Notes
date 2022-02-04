from django.shortcuts import render, redirect
from django.views import View

from djangoProject1.polls.models import Profile, Note


class ProfileView(View):
    def get(self, req):
        if Profile.objects.exists():
            current_user = Profile.objects.all()[0]
            notes = Note.objects.all().__len__()
            return render(req, "profile.html", {"user": current_user, "notes": notes})
        return redirect("/")

    def post(self, req):
        Profile.objects.all()[0].delete()
        Note.objects.all().delete()
        return redirect("/")
