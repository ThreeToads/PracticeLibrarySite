from django import template
from mainlibsite.models import *

register = template.Library()


@register.simple_tag(name='get_authors')
def get_author():
    return Author.objects.all()
