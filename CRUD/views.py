from rest_framework import viewsets
from .models import UsuarioNormal, Negocio, Categoria, Producto, Comentario, Respuesta, Likes, Calificacion
from .serializers import (
    UsuarioNormalSerializer, NegocioSerializer, CategoriaSerializer,
    ProductoSerializer, ComentarioSerializer, RespuestaSerializer, LikesSerializer, CalificacionSerializer
)

# ViewSet de Usuario Normal
class UsuarioNormalViewSet(viewsets.ModelViewSet):
    queryset = UsuarioNormal.objects.all()
    serializer_class = UsuarioNormalSerializer

# ViewSet de Negocio
class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

# ViewSet de Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# ViewSet de Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# ViewSet de Comentario
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

# ViewSet de Respuesta
class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer