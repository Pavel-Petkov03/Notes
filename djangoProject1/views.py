
from django.shortcuts import render



def home_no_profile(req):
    return render(req, "home-no-profile.html")