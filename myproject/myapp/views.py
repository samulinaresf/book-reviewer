from django.shortcuts import render
from django.shortcuts import render
from resumenes.models import Libro, Categoria, Autor
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
 
def index(request):
    libros = Libro.objects.all()
    mas_recientes = Libro.objects.order_by("-fecha")[:5]
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    if not libros:
        print("No se encontraron libros en la base de datos.")
    else:
        print("Libros encontrados:", libros)
    paginator = Paginator(libros,20)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    libros_count = libros.count()
    context = {
        'libros':libros_paginados,
        'mas_recientes':mas_recientes,
        'libros_count':libros_count,
        'categorias':categorias,
        'autores':autores
    }
    return render(request,'index.html',context)

def busqueda_producto(request):
    keyword = request.GET['keyword']
    libros = Libro.objects.none()  
    autor = Autor.objects.all()
    categorias = Categoria.objects.all()
    if keyword:
        libros = Libro.objects.filter(Q(titulo__icontains=keyword)|Q(id_autor__nombre__icontains=keyword)|Q(id_categoria__nombre__icontains=keyword)).order_by('titulo')
    print(f"Se han encontrado {libros.count()} libros")
    libros_count=libros.count()
    paginator = Paginator(libros, 2)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    context = {
        'libros':libros_paginados,
        'libros_count':libros_count,
        'autor':autor,
        'categorias':categorias
    }
    return render(request,'index.html',context)




