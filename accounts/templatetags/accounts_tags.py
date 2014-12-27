from django.template import Library
register = Library()


@register.simple_tag
def current_user():
    return "Dj radioweb"