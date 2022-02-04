from django import template

from djangoProject1.polls.models import Profile

register = template.Library()


@register.simple_tag()
def check_navbar():
    return Profile.objects.exists()
