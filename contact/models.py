from django.db import models

# Create your models here.


class Contact(models.Model):
  nombre   = models.CharField(max_length=40)
  telefono = models.CharField(max_length=40)
  correo   = models.CharField(max_length=40)
  mensaje  = models.TextField()
  
