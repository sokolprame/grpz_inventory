﻿from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='stock_operations_index'),
]