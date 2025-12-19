from django.test import TestCase
from contacto.models import Message
from contacto.contactform import ContactForm

class ContactoTestCase(TestCase):
    
    #Crear la base de datos
    def setUp(self):
      self.message = Message.objects.create(first_name="Juan",email="juan@juan.com",message="Este es un mensaje de prueba")
    
    #Comprobar el mensaje en la base de datos
    def test_mensaje_bbdd(self):
      self.assertIsInstance(Message.objects.get(first_name="Juan"),Message)
    
    #Comprobando si el formulario funciona  
    def test_form_valid(self):
      form_data = {"first_name":"Juan",
                   "email":"juan@juan.com",
                   "message":"Este es un mensaje de prueba"}
      form = ContactForm(data=form_data)
      self.assertTrue(form.is_valid(),form.errors)
      
    #Comprobando si el formulario no funciona  
    def test_form_invalid(self):
      form_data = {"first_name":"Juan",
                   "email":"juan",
                   "message":"Este es un mensaje de prueba"}
      form = ContactForm(data=form_data)
      self.assertFalse(form.is_valid(),form.errors)
      
  