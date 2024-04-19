from django.urls import path
from . import views

urlpatterns = [
    path('works_init', views.works_init, name='works_init'),
    path('works_insert', views.works_insert, name='works_insert'),
    path('works_delete', views.works_delete, name='works_delete'),
]