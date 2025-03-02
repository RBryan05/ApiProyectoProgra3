from rest_framework import viewsets
from .models import User, Business, Product, Service, Event, Review, SharedProduct, Promotion, SearchFilter
from .serializers import UserSerializer, BusinessSerializer, ProductSerializer, ServiceSerializer, EventSerializer, ReviewSerializer, SharedProductSerializer, PromotionSerializer, SearchFilterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SharedProductViewSet(viewsets.ModelViewSet):
    queryset = SharedProduct.objects.all()
    serializer_class = SharedProductSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class SearchFilterViewSet(viewsets.ModelViewSet):
    queryset = SearchFilter.objects.all()
    serializer_class = SearchFilterSerializer