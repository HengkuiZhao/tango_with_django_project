from django.urls import path
from rango import views
from rango import models

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('page/', models.Page, name='page'),
]
