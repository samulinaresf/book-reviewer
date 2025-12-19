from django.shortcuts import render,redirect
from contacto.models import Message
from django.forms import Form
from django import forms
from django.contrib import messages
from contacto.contactform import ContactForm

def contacto(request):
    return render(request, 'contacto.html')

def mensaje(request):
    try: 
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Mensaje enviado exitosamente")
                return redirect('contacto')
            else:
                messages.error(request, "No ha sido posible enviar el mensaje")
        else:
            form = ContactForm()
        return render(request, 'contacto.html', {'form': form})
        
    except Exception as e:
        messages.error(request,"Ocurrió un error inesperado")
        return render(request,'contacto.html',{'form':ContactForm()})