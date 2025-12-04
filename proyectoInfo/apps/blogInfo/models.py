from django.db import models
from django.contrib.auth.models import User as user
from django.utils import timezone

# Create your models here.
class Autor(models.Model):
    id_autor=models.BigAutoField(primary_key=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class post(models.Model):
    autor_post=models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_creacion=models.DateTimeField(default=timezone.now)
    fecha_actualizacion=models.DateTimeField(blank=True, null=True) 
    fecha_publicacion=models.DateTimeField( blank=True, null=True)
    categorias=models.ManyToManyField(Categoria, related_name='posts', blank=True)

    def __str__(self):
        return self.titulo
    
    def publicar_articulo(self):
        self.fecha_publicacion=timezone.now()
        self.save()

class Comentario(models.Model):
    autor_comentario= models.ForeignKey(user, on_delete=models.CASCADE)
    contenido_comentario=models.TextField()
    fecha_comentario=models.DateTimeField(default=timezone.now)
    post=models.ForeignKey(post,  related_name='comentarios', on_delete=models.CASCADE)

    comentario_padre=models.ForeignKey('self', blank=True, null=True, related_name='respuestas', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario de {self.autor_comentario} - {self.contenido_comentario[:30]}'
    
    