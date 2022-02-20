from django import template

from LibraryProject.library_app.models import Book, Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0


@register.simple_tag()
def get_profile():
    if has_profile:
        profile = Profile.objects.all()[0]
        return profile.first_name


@register.simple_tag()
def has_books():
    return Book.objects.count() > 0
