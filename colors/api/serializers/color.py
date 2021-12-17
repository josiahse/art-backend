from rest_framework import serializers
from ..models.color import Color

class ColorSerializer (serializers.ModelSerializer):
  class Meta:
    model = Color
    fields = ('id', 'name', 'color_list', 'owner')