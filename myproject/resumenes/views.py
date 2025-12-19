from django.shortcuts import render, redirect
from resumenes.models import Libro, Categoria, Autor
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
 
def mostrar_resumenes(request):
    libros = Libro.objects.filter()
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    if not libros:
        print("No se encontraron libros en la base de datos.")
    else:
        print("Libros encontrados:", libros)
    paginator = Paginator(libros,15)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    libros_count = libros.count()
    context = {
        'libros':libros_paginados,
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
    paginator = Paginator(libros, 15)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    context = {
        'libros':libros_paginados,
        'libros_count':libros_count,
        'autor':autor,
        'categorias':categorias
    }
    return render(request,'index.html',context)

@login_required
def puntuar_libro(request,libro_id,x):
    if request.method == "POST":
        libro = Libro.objects.get(pk=libro_id)
        libro.num_valoraciones += 1
        estrellas = int(x)
        libro.num_estrellas += estrellas
        libro.save()
        print("Valoración:",libro.valoracion)
        return redirect(mostrar_resumenes)
    return redirect(mostrar_resumenes)



