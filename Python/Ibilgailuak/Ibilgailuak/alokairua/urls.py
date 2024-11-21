from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.kotxe_zerrenda, name='kotxe_zerrenda'),
    path('alokatu/<int:kotxe_id>/', views.kotxe_alokatu, name='kotxe_alokatu'),
]