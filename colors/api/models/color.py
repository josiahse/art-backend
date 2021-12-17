from django.db import models
from django.contrib.auth import get_user_model

class Color(models.Model):
  name = models.CharField(max_length=100)
  color_list = models.CharField(max_length=100000)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} is owned by {self.owner}"