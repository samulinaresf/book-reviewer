from django.test import TestCase
from resumenes.models import Libro,Autor,Categoria

# Create your tests here.
class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(nombre="Nuevo Autor", slug="nuevo-autor")
    def test_object_created(self):
        self.assertTrue(Autor.objects.filter(slug="nuevo-autor").exists(),"Prueba test: Autor creado exitosamente.")
        
class CategoriaTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(nombre="Nueva Categoria", slug="nueva-categoria")
    def test_object_created(self):
        self.assertTrue(Categoria.objects.filter(slug="nueva-categoria").exists(),"Prueba test: Categoria creada exitosamente.")

class LibroTestCase(TestCase):
    def setUp(self):
        self.autor=Autor.objects.create(nombre="Nuevo Autor", slug="nuevo-autor")
        self.categoria=Categoria.objects.create(nombre="Nueva Categoria", slug="nueva-categoria")
        Libro.objects.create(titulo="libro de prueba", slug="libro-de-prueba",id_autor=self.autor, slug_autor=self.autor.slug, id_categoria=self.categoria, slug_categoria=self.categoria.slug, fecha=20250210, valoracion=1)
        
    def test_slug_autor(self):
        libro = Libro.objects.get(slug="libro-de-prueba")
        self.assertEqual(libro.id_autor.slug, "nuevo-autor", "El slug del autor no coincide.")
            
    def test_slug_categoria(self):
        libro = Libro.objects.get(slug="libro-de-prueba")
        self.assertEqual(libro.id_categoria.slug, "nueva-categoria", "El slug de la categoria no coincide.")
            
    def test_object_created(self):
        self.assertTrue(Libro.objects.filter(slug="libro-de-prueba").exists(),"Prueba test: Libro creado exitosamente.")
