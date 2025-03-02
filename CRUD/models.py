from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuario
class User(AbstractUser):
    email = models.EmailField(unique=True)
    google_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    saved_products = models.ManyToManyField('Product', related_name='saved_by_users', blank=True, null=True)

    # Cambiar related_name para evitar conflictos con el modelo de usuario predeterminado
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Un nombre único para evitar conflicto
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Un nombre único para evitar conflicto
        blank=True
    )

# Negocio
class Business(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='business_photos/')
    category = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    product_categories = models.TextField()
    contact_number = models.CharField(max_length=15)
    facebook_contact = models.URLField()
    website = models.URLField()
    has_shipping = models.BooleanField(default=False)

# Producto
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='product_photos/')
    video_review = models.URLField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    brand = models.CharField(max_length=255)
    status = models.BooleanField(default=True)  # Activado o Desactivado
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='products')

# Servicio
class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField()
    materials_used = models.TextField()
    estimated_time = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    service_area = models.CharField(max_length=255)

# Evento
class Event(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='event_photos/')
    description = models.TextField()
    businesses = models.ManyToManyField(Business, related_name='events')
    video_url = models.URLField(blank=True, null=True)

# Comentarios y Calificaciones
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.IntegerField()  # 1-5 estrellas
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Compartidos
class SharedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

# Promociones
class Promotion(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='promotions')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

# Filtros de búsqueda
class SearchFilter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, blank=True, null=True)
    price_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    last_search_at = models.DateTimeField(auto_now=True)