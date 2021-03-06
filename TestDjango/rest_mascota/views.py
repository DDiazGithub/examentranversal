from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Mascota
from .serializers import MascotaSerializer
@csrf_exempt
@api_view(['GET','POST'])
def api_mascotas(request):
    """
    Lista de las mascotas
    """
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        serializer = MascotaSerializer(mascota, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def info_mascotas(request, id):
    """
    get update delete de una mascota
    """
    try:
        mascota = Mascota.objects.get (nombre=id)
    except Mascota.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(mascota, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        