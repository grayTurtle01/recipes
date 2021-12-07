from django import template

register = template.Library()

def split(text, sep):
  return text.split(sep)


register.filter('split', split)