from django import template

register = template.Library()

# return an array of string 
def split(text, sep):
  words = text.split(sep)
  clean_words = []

  for word in words:
    clean_word = word.strip(' ')
    clean_words.append(clean_word)

  return clean_words

register.filter('split', split)