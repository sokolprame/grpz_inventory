from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path('', views.component_list, name='component_list'),
    path('add/', views.add_component, name='add_component'),
    path('<int:pk>/', views.component_detail, name='component_detail'),  # Добавляем маршрут для деталей
]