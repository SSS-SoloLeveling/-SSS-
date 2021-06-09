from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
]