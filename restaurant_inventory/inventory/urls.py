from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('list_ingredients/', views.list_ingredients, name='list_ingredients'),  # Listado de ingredientes
    path('list_products/', views.list_products, name='list_products'),  # Listado de productos
    path('list_recipes/', views.list_recipes, name='list_recipes'),  # Listado de recetas
]