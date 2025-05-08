from django.urls import path
from . import views

urlpatterns = [
    path('', views.components_list, name='components_list'),
    path('<int:pk>/', views.component_detail, name='component_detail'),
]