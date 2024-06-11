from django.urls import path
from .views import *


urlpatterns = [
    path('search/<int:pk>/', search_form, name='search_form'),
    path('results/<int:pk>/', results, name='results'),
    path('history/<int:pk>/', history, name='history'),
    path('history_results/<int:pk>/<int:id>', history_results, name='history_results'),
]