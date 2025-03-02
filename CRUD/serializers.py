from rest_framework import serializers
from .models import User, Business, Product, Service, Event, Review, SharedProduct, Promotion, SearchFilter

# Serializer de Usuario
class UserSerializer(serializers.ModelSerializer):
    saved_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'saved_products']

# Serializer de Negocio
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = [
            'id', 'name', 'schedule', 'photo', 'category', 'slogan', 
            'address', 'latitude', 'longitude', 'product_categories', 
            'contact_number', 'facebook_contact', 'website', 'has_shipping'
        ]

# Serializer de Producto
class ProductSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'stock', 'category', 'photo', 
            'video_review', 'sku', 'description', 'brand', 'status', 'business'
        ]

# Serializer de Servicio
class ServiceSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'business', 'name', 'description', 'materials_used', 'estimated_time', 'category', 'service_area']

# Serializer de Evento
class EventSerializer(serializers.ModelSerializer):
    businesses = BusinessSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'type', 'address', 'latitude', 'longitude', 'start_time', 'end_time', 'entry_price', 
                  'photo', 'description', 'businesses', 'video_url']

# Serializer de Comentario y Calificación
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True, required=False)
    business = BusinessSerializer(read_only=True, required=False)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'business', 'rating', 'comment', 'created_at']

# Serializer de Producto Compartido
class SharedProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SharedProduct
        fields = ['id', 'user', 'product', 'shared_at']

# Serializer de Promoción
class PromotionSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'business', 'description', 'start_date', 'end_date']

# Serializer de Filtro de Búsqueda
class SearchFilterSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SearchFilter
        fields = ['id', 'user', 'category', 'price_min', 'price_max', 'product_name', 'location', 'last_search_at']