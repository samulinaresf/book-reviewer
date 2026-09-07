from django.shortcuts import render, redirect
from resumenes.models import Libro, Categoria, Autor, LibroUsuario
from accounts.models import Account
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .servicios.google_books import buscar_libros_google
 
def mostrar_resumenes(request):
    libros = Libro.objects.filter()
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    if not libros:
        print("No se encontraron libros en la base de datos, utiliza el buscador para buscar el libro en Google Books.")
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

@login_required
def mostrar_libros_favoritos(request):
    libros = LibroUsuario.objects.filter(usuario=request.user)
    if not libros:
        print("No se encontraron libros en favoritos.")
    else:
        print("Libros encontrados:", libros)
    paginator = Paginator(libros,15)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    libros_count = libros.count()
    context = {
        'favoritos':libros_paginados,
        'libros_count':libros_count,
    }
    return render(request,'perfil.html',context)

def busqueda_producto(request):
    keyword = request.GET.get('keyword', '')
    pagina = int(request.GET.get('page', 1))

    libros = Libro.objects.none() 
    libros_google = []
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    if keyword:
        libros = Libro.objects.filter(Q(titulo__icontains=keyword)|Q(autores__nombre__icontains=keyword)|Q(categorias__nombre__icontains=keyword)).distinct().order_by('titulo')
        libros_google = buscar_libros_google(keyword, pagina=pagina)
    print(f"Se han encontrado {libros.count()} libros")
    libros_count = libros.count() + len(libros_google)
    paginator = Paginator(libros, 15)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    context = {
        'libros':libros_paginados,
        'libros_count':libros_count,
        'libros_google': libros_google,
        'autores':autores,
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

@login_required
def agregar_favoritos(request,libro_id):
    if request.method == "POST":
        libro = Libro.objects.get(pk=libro_id)
        libro_usuario, creado = LibroUsuario.objects.get_or_create(
            usuario=request.user,
            libro=libro
        )

        if creado:
            print("Añadido a favoritos:", libro_usuario.libro.titulo)
        else:
            print("El libro ya estaba en favoritos:", libro_usuario.libro.titulo)

        return redirect(mostrar_resumenes)
    return redirect(mostrar_resumenes)

def buscar_libros_google_books(request):

    query = request.GET.get("q")
    books = []
    if query:
        books = buscar_libros_google(query)
    return render(
        request,
        "books/search_results.html",
        {
            "books": books,
            "query": query,
        }
    )



