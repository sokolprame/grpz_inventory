from django.urls import path
from . import views

app_name = 'warehouses'

urlpatterns = [
    path('', views.warehouse_list, name='warehouse_list'),
    path('create/', views.warehouse_create, name='warehouse_create'),
    path('edit/<int:pk>/', views.warehouse_edit, name='warehouse_edit'),
]