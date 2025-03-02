from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, BusinessViewSet, ProductViewSet, 
    ServiceViewSet, EventViewSet, ReviewViewSet, 
    SharedProductViewSet, PromotionViewSet, SearchFilterViewSet
)

router = DefaultRouter()
router.register('api/users', UserViewSet)
router.register('api/businesses', BusinessViewSet)
router.register('api/products', ProductViewSet)
router.register('api/services', ServiceViewSet)
router.register('api/events', EventViewSet)
router.register('api/reviews', ReviewViewSet)
router.register('api/shared-products', SharedProductViewSet)
router.register('api/promotions', PromotionViewSet)
router.register('api/search-filters', SearchFilterViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto incluirá todas las rutas del enrutador bajo el prefijo /api/
]