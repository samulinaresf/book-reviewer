from django import forms
from contacto.models import Message
from django.contrib.auth import authenticate

class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['first_name', 'email', 'message']
        labels = {
            'first_name': 'Nombre',
            'email': 'Email',
            'message': 'Mensaje',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí'}),
        }

    def save(self, commit=True):
        user = super(ContactForm, self).save(commit=False)
        if commit:
            user.save()
        return user
