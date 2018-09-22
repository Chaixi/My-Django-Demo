from django import template
from django.utils.html import format_html
import datetime
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='get_list')
def get_list(value):
    return range(value-2, value+2)

# register.filter(get_list)