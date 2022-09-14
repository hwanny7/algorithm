from django.contrib import admin
from django.urls import path
from . import views

app_name = 'calculators'
urlpatterns = [
    path('calculator/<int:pk>/', views.calculators, name='calculators'),
]
