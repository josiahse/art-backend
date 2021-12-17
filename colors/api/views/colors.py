from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.color import ColorSerializer
from ..models.color import Color

class ColorsView(APIView):
  def get(self, request):
    colors = Color.objects.filter(owner = request.user.id)
    data = ColorSerializer(colors, many=True).data
    return Response(data)

  def post(self, request):
    request.data['owner'] = request.user.id
    color = ColorSerializer(data=request.data)
    if color.is_valid():
      color.save()
      return Response(color.data, status=status.HTTP_201_CREATED)
    else:
      return Response(color.errors, status=status.HTTP_400_BAD_REQUEST)

class ColorView(APIView):
  def delete(self, request, pk):
    color = get_object_or_404(Color, pk=pk)
    if request.user != color.owner:
      raise PermissionDenied("These are not the colors you're looking for.")
    color.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get(self, request, pk):
    color = get_object_or_404(Color, pk=pk)
    if request.user != color.owner:
      raise PermissionDenied("These are not the colors you're looking for.")
    data = ColorSerializer(color).data
    return Response(data)
  
  def patch(self, request, pk):
    color = get_object_or_404(Color, pk=pk)
    if request.user != color.owner:
      raise PermissionDenied("These are not the colors you're looking for.")
    request.data['owner'] = request.user.id
    updated_color = ColorSerializer(color, data = request.data)
    if updated_color.is_valid():
      updated_color.save()
      return Response(updated_color.data)
    return Response(updated_color.errors, status=status.HTTP_400_BAD_REQUEST)
