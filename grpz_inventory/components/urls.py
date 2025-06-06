from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path('', views.component_list, name='component_list'),
    path('add/', views.add_component, name='add'),
    path('<int:pk>/', views.component_detail, name='component_detail'),
    path('<int:pk>/edit/', views.edit_component, name='edit'),  # Новый маршрут для редактирования
    path('<int:pk>/delete/', views.delete_component, name='delete'),  # Новый маршрут для удаления
]