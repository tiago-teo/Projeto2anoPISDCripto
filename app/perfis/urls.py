from django.urls import path
from .views import *

urlpatterns = [    
    path('perfil/<int:pk>/edit/', perfil_update, name='perfil_update'),    
]
