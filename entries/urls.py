from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path ('search/', views.search, name='search'),
    path ('add/', views.add, name='add'),
    path ('upload/', views.upload, name= 'upload'),
         
]

