from django.urls import path, include

from . import views

urlpatterns = [
    path('receita', views.receita, name='receita'),
    path('', views.index, name='index')
]