from django.db import models
from django import forms

class Message(models.Model):
    first_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    message = models.CharField(max_length=5000)
    
    class Meta:
        db_table = 'mensajes'              
        managed = True