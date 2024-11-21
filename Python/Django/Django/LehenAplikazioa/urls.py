from django.urls import path
from . import views

urlpatterns = [
 path('', views.ikasle_list, name='zerrenda-default'),
 path('Ikasle/new/', views.gehitu_ikaslea, name='ikasle-gehitu'),
 path('Notak/new/', views.nota_sartu, name='nota-sartu'),
 path('Notak/zerrenda/', views.nota_zerrenda, name='nota-zerrenda'),
 path('Notak/aldatu/<int:nota_id>/', views.nota_aldatu, name='nota-aldatu'),
 path('Ikasgaia/new/', views.gehitu_ikasgaia, name='ikasgaia-gehitu'),
 path('Ikasle/zerrenda/', views.ezabatu_zerrenda, name='ezabatu-zerrenda'),
 path('Ikasle/delete/<int:id>/', views.ezabatu_ikaslea, name='ikasle-ezabatu'),
]