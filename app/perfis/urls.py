from django.urls import path
from .views import *

urlpatterns = [
    path('', perfil_list, name='perfil_list'),
    path('perfil/<int:pk>/', perfil_detail, name='perfil_detail'),
    path('perfil/new/', perfil_create, name='perfil_create'),
    path('perfil/<int:pk>/edit/', perfil_update, name='perfil_update'),
    path('perfil/<int:pk>/delete/', perfil_delete, name='perfil_delete'),
]
