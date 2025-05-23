from django.db import models

# Modelo de Usuario Normal
class UsuarioNormal(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)  # Nombre de usuario único
    nombre = models.CharField(max_length=255)  # Nombre del usuario, puede repetirse
    password = models.CharField(max_length=255)
    foto_perfil = models.URLField(max_length=1000,null=True, blank=True)  # Enlace de la foto de perfil
    productos_favoritos = models.JSONField(null=True, blank=True)  # Array de IDs de productos favoritos
    tipo_usuario = models.CharField(max_length=50, default='normal', editable=False)  # Tipo de usuario, por defecto 'normal'

    def __str__(self):
        return self.nombre_usuario

# Modelo de Negocio
class Negocio(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)  # Nombre de usuario único
    nombre = models.CharField(max_length=255)  # Nombre del negocio, puede repetirse
    direccion = models.CharField(max_length=455, blank=True)  # Dirección del negocio
    descripcion = models.TextField(max_length=200, null=True, blank=True)  # Descripción del negocio
    telefono = models.CharField(max_length=20, null=True, blank=True)  # Teléfono del negocio
    password = models.CharField(max_length=255)
    foto_perfil = models.URLField(max_length=1000,null=True, blank=True)  # Enlace de la foto de perfil
    productos_favoritos = models.JSONField(null=True, blank=True)  # Array de IDs de productos favoritos
    tipo_usuario = models.CharField(max_length=50, default='negocio', editable=False)  # Tipo de usuario, por defecto 'negocio'

    def __str__(self):
        return self.nombre

# Modelo de Categoría de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    imagen_url = models.URLField(max_length=1000, null=True, blank=True)  # Enlace de la imagen de la categoría
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, related_name='categorias')  # Relación con el negocio

    def __str__(self):
        return self.nombre

# Modelo de Producto
class Producto(models.Model):
    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Precio del producto
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=1000, null=True, blank=True)  # Enlace de la imagen del producto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, related_name='productos')
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Calificacion(models.Model):
    id_usuario = models.ForeignKey(UsuarioNormal, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], default=0)

class Likes(models.Model):
    id_usuario = models.ForeignKey(UsuarioNormal, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

# Modelo de Comentarios
from django.core.exceptions import ValidationError
from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey('UsuarioNormal', on_delete=models.CASCADE, null=True, blank=True)
    negocio = models.ForeignKey('Negocio', on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    calificacion = models.PositiveIntegerField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], default=5, null=True, blank=True)  # Calificación opcional
    esRespuesta = models.BooleanField(default=False)  # Indica si es una respuesta a otro comentario
    comentario_respuesta = models.IntegerField(null=True, blank=True)  # ID del comentario al que responde
    creado_en = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.usuario and self.negocio:
            raise ValidationError("Un comentario no puede tener tanto un usuario como un negocio asignado. Debe ser uno solo.")
        if not self.usuario and not self.negocio:
            raise ValidationError("Debe asignarse un usuario o un negocio como autor del comentario.")

    def __str__(self):
        autor = self.usuario.nombre_usuario if self.usuario else self.negocio.nombre_negocio if self.negocio else "Sin autor"
        return f'Comentario de {autor} en {self.producto.nombre}'
