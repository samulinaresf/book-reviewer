from django.db import models
from django.conf import settings

#Categorías de los libros
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        db_table = 'categoria'  
        managed = True

#Autores de los libros
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    class Meta:
        db_table = 'autor'              
        managed = True

#Libros
class Libro(models.Model):
    google_books_id = models.CharField(max_length=50,unique=True,null=True,blank=True)
    titulo = models.CharField(max_length=255)
    autores = models.ManyToManyField(Autor,related_name="libros",blank=True)
    descripcion = models.TextField(null=True, blank=True)
    editorial = models.CharField(max_length=255,null=True,blank=True)
    fecha_publicacion = models.CharField(max_length=20,null=True,blank=True)
    paginas = models.PositiveIntegerField(null=True, blank=True)    
    google_valoracion = models.FloatField(null=True,blank=True)
    google_num_valoraciones = models.PositiveIntegerField(default=0)
    categorias = models.ManyToManyField(Categoria,related_name="libros",blank=True)
    num_estrellas = models.PositiveIntegerField(default=0)
    num_valoraciones = models.PositiveIntegerField(default=0)
    portada = models.URLField(null=True,blank=True)
    isbn_10 = models.CharField(max_length=10,null=True,blank=True)
    isbn_13 = models.CharField(max_length=13,null=True,blank=True,db_index=True)
    idioma = models.CharField(max_length=10,null=True,blank=True)

    class Meta:
        db_table = 'libro'  
        managed = True
    
    @property
    def valoracion(self):
        if self.num_valoraciones > 0:
            valoracion = self.num_estrellas / self.num_valoraciones
            return valoracion
        return 0
    

class LibroUsuario(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="libros_usuario"
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="usuarios_libro"
    )

    class Meta:
        db_table = "libro_usuario"
        managed = True
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "libro"],
                name="unique_usuario_libro"
            )
        ]