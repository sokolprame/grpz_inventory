from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('audit/', include('audit.urls')),
    path('components/', include('components.urls')),
    path('orders/', include('orders.urls')),
    path('stock_operations/', include('stock_operations.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('users/', include('users.urls')),
    path('warehouses/', include('warehouses.urls')),
    path('admin/', admin.site.urls),
]