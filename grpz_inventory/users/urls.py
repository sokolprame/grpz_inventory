from django.urls import path
from grpz_inventory import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]