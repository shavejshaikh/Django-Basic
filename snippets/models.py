from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# LEXER
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.

class Snippet(models.Model):
    title  = models.CharField(max_length=100,default=None)
    author = models.CharField(max_length=100,default=None)
    email  = models.EmailField(max_length=100,default=None)
    date   = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.title

