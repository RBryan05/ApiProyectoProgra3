from django.db import models

# Modelo de Usuario Normal
class UsuarioNormal(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)  # Nombre de usuario único
    nombre = models.CharField(max_length=255)  # Nombre del usuario, puede repetirse
    password = models.CharField(max_length=255)
    foto_perfil = models.URLField(null=True, blank=True)  # Enlace de la foto de perfil
    productos_favoritos = models.JSONField(null=True, blank=True)  # Array de IDs de productos favoritos
    tipo_usuario = models.CharField(max_length=50, default='normal', editable=False)  # Tipo de usuario, por defecto 'normal'

    def __str__(self):
        return self.nombre_usuario

# Modelo de Negocio
class Negocio(models.Model):
    nombre_usuario = models.CharField(max_length=255, unique=True)  # Nombre de usuario único
    nombre = models.CharField(max_length=255)  # Nombre del negocio, puede repetirse
    direccion = models.CharField(max_length=455, blank=True)  # Dirección del negocio
    password = models.CharField(max_length=255)
    foto_perfil = models.URLField(null=True, blank=True)  # Enlace de la foto de perfil
    productos_favoritos = models.JSONField(null=True, blank=True)  # Array de IDs de productos favoritos
    tipo_usuario = models.CharField(max_length=50, default='negocio', editable=False)  # Tipo de usuario, por defecto 'negocio'

    def __str__(self):
        return self.nombre

# Modelo de Categoría de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
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
    imagen_url = models.URLField(max_length=500, null=True, blank=True)  # Enlace de la imagen del producto
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
class Comentario(models.Model):
    usuario = models.ForeignKey(UsuarioNormal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    calificacion = models.PositiveIntegerField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], default=5)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.nombre_usuario} en {self.producto.nombre}'

# Modelo de Respuestas a Comentarios (Solo negocios pueden responder)
class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    texto = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta de {self.negocio.nombre_usuario} a {self.comentario.usuario.nombre_usuario}'
