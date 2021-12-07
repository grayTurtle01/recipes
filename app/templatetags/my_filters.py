from django import template

register = template.Library()

def split(text, sep):
  #text = text.replace(' ', '')
  return text.split(sep)


register.filter('split', split)