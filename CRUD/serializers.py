from rest_framework import serializers
from .models import UsuarioNormal, Negocio, Categoria, Producto, Comentario, Respuesta, Likes, Calificacion

# Serializer de Usuario Normal
class UsuarioNormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioNormal
        fields = ['id', 'nombre_usuario', 'nombre', 'password', 'foto_perfil', 'productos_favoritos', 'tipo_usuario']

# Serializer de Negocio
class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ['id', 'nombre_usuario', 'nombre', 'direccion', 'password', 'foto_perfil', 'productos_favoritos', 'tipo_usuario']

# Serializer de Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    negocio_id = serializers.PrimaryKeyRelatedField(queryset=Negocio.objects.all(), source='negocio')  # Permite recibir el ID del negocio

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'negocio_id']  # 'negocio' se cambia por 'negocio_id' para manejar el ID

class LikesSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=UsuarioNormal.objects.all())  # Relación con el usuario
    id_producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())  # Relación con el producto

    class Meta:
        model = Likes
        fields = ['id', 'id_usuario', 'id_producto', 'like']

class CalificacionSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=UsuarioNormal.objects.all())  # Relación con el usuario
    id_producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())  # Relación con el producto

    # Validar que la calificación esté entre 1 y 5
    def validate_calificacion(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe ser entre 1 y 5.")
        return value

    class Meta:
        model = Calificacion
        fields = ['id', 'id_usuario', 'id_producto', 'calificacion']

# Serializer de Producto
class ProductoSerializer(serializers.ModelSerializer):
    # Relacionar negocio y categoria por sus IDs
    negocio_id = serializers.PrimaryKeyRelatedField(queryset=Negocio.objects.all(), source='negocio')
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen_url', 'estado', 'negocio_id', 'categoria_id', 'creado_en', 'actualizado_en']

    def create(self, validated_data):
        negocio = validated_data.pop('negocio')
        categoria = validated_data.pop('categoria')
        producto = Producto.objects.create(negocio=negocio, categoria=categoria, **validated_data)
        return producto

# Serializer de Comentario
class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=UsuarioNormal.objects.all())  # Aseguramos la relación con el usuario
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())  # Relacionamos con el producto

    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'producto', 'texto', 'calificacion', 'creado_en']

# Serializer de Respuesta
class RespuestaSerializer(serializers.ModelSerializer):
    comentario = serializers.PrimaryKeyRelatedField(queryset=Comentario.objects.all())  # Relación con el comentario
    negocio = serializers.PrimaryKeyRelatedField(queryset=Negocio.objects.all())  # Relación con el negocio

    class Meta:
        model = Respuesta
        fields = ['id', 'comentario', 'negocio', 'texto', 'creado_en']
