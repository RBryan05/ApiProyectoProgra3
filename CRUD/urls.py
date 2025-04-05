from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioNormalViewSet, NegocioViewSet, CategoriaViewSet,
    ProductoViewSet, ComentarioViewSet, RespuestaViewSet
)

router = DefaultRouter()
router.register('api/usuarios', UsuarioNormalViewSet)
router.register('api/negocios', NegocioViewSet)
router.register('api/categorias', CategoriaViewSet)
router.register('api/productos', ProductoViewSet)
router.register('api/comentarios', ComentarioViewSet)
router.register('api/respuestas', RespuestaViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto incluirá todas las rutas del enrutador bajo el prefijo /api/
]
