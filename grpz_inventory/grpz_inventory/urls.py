﻿from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('audit/', include('audit.urls')),
    path('components/', include('components.urls')),
    path('orders/', include('orders.urls')),
    path('stock_operations/', include('stock_operations.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('warehouses/', include('warehouses.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('users/', include('users.urls', namespace='users')),  # Все пользовательские маршруты здесь
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)