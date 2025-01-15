from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Product, Recipe
# Create your views here.
# Vista para la página de inicio
def home(request):
    return render(request, 'inventory/home.html')

# Vista para registrar un usuario
def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
        else:
            form = UserCreationForm()
    return render(request, 'inventory/register.html',{ 'form':form })

# Vista para iniciar sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
           login(request, form.get_user())
           return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('home')

# Vista de perfil de usuario (solo accesible si está logueado)
@login_required
def profile(request):
    return render(request, 'inventory/profile.html')

# Vista para listar ingredientes
@login_required
def list_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/list_ingredients.html', {'ingredients': ingredients})

# Vista para listar productos
@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'inventory/list_products.html', {'products': products})

# Vista para listar recetas
@login_required
def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'inventory/list_recipes.html', {'recipes': recipes})