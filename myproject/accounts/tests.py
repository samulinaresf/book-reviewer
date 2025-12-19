from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Account
from accounts.forms import RegistrationForm, LoginForm
from django.test import TestCase
from django.middleware.csrf import get_token
from django.contrib.auth import get_user
from django.test.utils import override_settings

class AccountTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create(
            first_name="Juanito",
            last_name = "Juanito",
            email="juanito@juanito.com",
            username="juanito",
            phone_number="12345",
            date_birth="1999-02-02",
            is_member=False,
            membership_date="2025-02-15",
            date_joined="2025-02-15",
            last_login="2025-02-15",
            is_active=True,
            is_staff=False,
            is_admin=False,
            is_superuser=False)
        self.user.set_password("1234567")
        self.user.save()
    
    #Comprobando que acepta los login correctos    
    def test_login_valid(self):
        form = self.client.login(username="juanito",password="1234567")
        self.assertTrue(form)
    
    #Comprobando que acepta los login correctos       
    def test_login_invalid(self):
        form = self.client.login(username="juanito",password="wrongpassword")
        self.assertFalse(form)
    
    #Comprobando que acepta los formularios de registro correctos       
    def test_registration_form_valid(self):
        form_data = {
            "first_name":"Ejemplo",
            "last_name":"Ejemplo",
            "email":"ejemplo12345@ejemplo.com",
            "username":"ejemplo12345",
            "date_birth":"2025-02-01",
            "password1":"ejemplo1234",
            "password2":"ejemplo1234"}
        
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid(),form.errors)

#Comprobando que rechaza los formularios de registro incorrectos       
    def test_registration_form_invalid(self):
        form_data = {
            "first_name":"Ejemplo",
            "last_name":"Ejemplo",
            "email":"ejemplo12345@ejemplo.com",
            "username":"ejemplo12345",
            "date_birth":"2025-02-01",
            "password1":"ejemplo1234",
            "password2":"wrongpassword"}
        
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid(),form.errors)
       
    #Comprobando que se puede hacer logout 
    def test_logout(self):
        self.client.login(username="juanito",password="1234567")
        response = self.client.post(reverse("cerrar-sesion"))
        self.assertRedirects(response, reverse("inicio-sesion"))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        
#Comprobando la seguridad CSRF
class CSRFMiddlewareTest(TestCase):
    
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
    
    # Comprobando que rechaza solicitudes sin CSRF tokens
    def test_csrf_protection(self):
        url = reverse("ruta-protegida")  # Ruta de la vista protegida por CSRF
        response = self.client.post(url, {})  # Hacemos un POST sin CSRF

        # Asegurar que la respuesta sea 403 Forbidden, indicando que CSRF ha bloqueado la petición
        self.assertEqual(response.status_code, 403, f"La solicitud sin CSRF debería ser rechazada con 403, pero obtuvo {response.status_code}")

@override_settings(CSRF_USE_SESSIONS=False, CSRF_COOKIE_SECURE=False)

class CSRFSecureTest(TestCase):
    
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_valid_csrf_token(self):

        #response = self.client.get('/accounts/ruta-protegida/')
        url = reverse('ruta-protegida')
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 404, "La vista '/accounts/ruta-protegida/' no existe.")

        self.assertIn('csrftoken', response.cookies, "No se encontró el token CSRF en las cookies")

        csrf_token = response.cookies['csrftoken'].value  

        response = self.client.post(url, 
                                    {'campo': 'valor'}, 
                                    HTTP_X_CSRFTOKEN=csrf_token)

        self.assertIn(response.status_code, [200, 302])


"""
# Desactivar el CSRF token para probar alguna API 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def vista_sin_csrf(request):
    return JsonResponse({"mensaje": "Sin protección CSRF"})"""

    
    
        
        
    
