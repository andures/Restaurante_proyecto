from django.db import models
from django.contrib.auth.models import User
# Create your models here.pytho
# Modelo para los Ingredientes
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)  # Unidad de medida, como 'kg', 'l', etc.

    def __str__(self):
        return self.name

# Modelo para los Productos (Menú)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Modelo para las Recetas (Relación entre Producto e Ingredientes)
class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()  # Cantidad del ingrediente en la receta

    def __str__(self):
        return f"{self.product.name} - {self.ingredient.name}"

# Modelo para las Compras (Registro de compras de productos)
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} unidades"