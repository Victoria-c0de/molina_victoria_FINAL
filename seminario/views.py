from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .models import Inscrito
from .serializers import InscritoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


#pagina principal
def index(request):
    # Recupera la lista de inscritos
    inscritos = Inscrito.objects.all()
    # Pasa la lista de inscritos a la plantilla HTML
    return render(request, 'index.html', {'inscritos': inscritos})

def get_autor_info(request):
    autor_info = {
        'name': 'Victoria Molina Copier',
        'asignatura': 'backend',
        'Profesor': 'Pedro Gaete',
        'secciones': '(TI2041/AP-171-N4/D Temuco B5 )',
        'github': 'https://github.com/Victoria-c0de',
        # Agrega cualquier otra información del autor que desees mostrar
    }
    return JsonResponse(autor_info)


# CLASS BASED VIEWS 
#Lista de Participantes, creacion de nuevos
class InscritoListCreateView(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#detalles de participantes
class InscritoDetailView(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)
    
    def put(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FUNCTION BASED VIEWS
#maneja la lista de participantes 

@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#obtiene los detalles del participante por su id 
@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detail(request, id):
    try:
        inscrito = Inscrito.objects.get(pk=id)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
