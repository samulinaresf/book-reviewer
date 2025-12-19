from django import forms
from accounts.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
    label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}),
    label="Repetir contraseña")

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'username', 'date_birth']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'username': 'Nombre de usuario',
            'date_birth': 'Fecha de nacimiento',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)  # El backend personalizado usará el email
            if user is None:
                raise forms.ValidationError("Email o contraseña incorrectos")
        return self.cleaned_data