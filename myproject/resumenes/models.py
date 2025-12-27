from django.db import models
from django.utils import timezone

# Creando los modelos

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
    isbn = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    id_autor = models.ForeignKey(Autor, db_column="id_autor", on_delete=models.CASCADE,related_name="libros_por_autor",default=1)
    id_categoria = models.ForeignKey(Categoria, db_column="id_categoria", on_delete=models.CASCADE,related_name="libros_por_categoria",default=1)
    fecha = models.DateField(default=timezone.now())
    link = models.URLField(blank=True)
    num_valoraciones = models.IntegerField(default=0)
    num_estrellas = models.IntegerField(default=0)
    resumen = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'libro'  
        managed = True
    
    @property
    def valoracion(self):
        if self.num_valoraciones > 0:
            valoracion = self.num_estrellas / self.num_valoraciones
            return valoracion
        return 0
        
