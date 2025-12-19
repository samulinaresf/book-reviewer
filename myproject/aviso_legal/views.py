from django.shortcuts import render

def aviso_legal(request):
    return render(request, 'aviso_legal.html')
