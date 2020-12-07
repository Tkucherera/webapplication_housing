from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.home, name='home'), path('about/', views.about, name='about'),
    path('athletes/', views.athletes, name='athletes'),
    path('contact/', views.contact, name='contact'), path('honors/', views.honors, name='honors'),
    path('news/', views.news, name='news'), path('issue/', views.issues, name='issues'),
    path('residences/', views.residence, name='residence'), path('apply/', views.apply, name='apply'),
]
