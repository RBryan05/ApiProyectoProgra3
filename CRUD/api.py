from rest_framework import viewsets, permissions
from .models import User, Business, Product, Service, Event, Review, SharedProduct, Promotion, SearchFilter
from .serializers import UserSerializer, BusinessSerializer, ProductSerializer, ServiceSerializer, EventSerializer, ReviewSerializer, SharedProductSerializer, PromotionSerializer, SearchFilterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    serializer_class = UserSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitido para cualquier persona
    serializer_class = BusinessSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitido para cualquier persona
    serializer_class = ProductSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitido para cualquier persona
    serializer_class = ServiceSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitido para cualquier persona
    serializer_class = EventSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    serializer_class = ReviewSerializer

class SharedProductViewSet(viewsets.ModelViewSet):
    queryset = SharedProduct.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    serializer_class = SharedProductSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitido para cualquier persona
    serializer_class = PromotionSerializer

class SearchFilterViewSet(viewsets.ModelViewSet):
    queryset = SearchFilter.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    serializer_class = SearchFilterSerializer