from pyexpat import model
from xml.sax import default_parser_list
from django.db import models

# Create your models here.

class Movie(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  active = models.BooleanField(default=True)

  def __str__(self) -> str:
      return self.name

