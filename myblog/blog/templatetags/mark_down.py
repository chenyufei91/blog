from django import template
from django.utils.html import strip_tags
import markdown

register = template.Library()


#
# @register.filter
# def mark_down(value):
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#
#     ])
#     value = strip_tags(md.convert(value))
#     return value
