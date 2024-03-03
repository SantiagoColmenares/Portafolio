
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "inicio"), 
    path('Portafolio/', views.portafolio, name="portafolio"),
    path('Contacto/', views.contacto, name="contacto")
]
