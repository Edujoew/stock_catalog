from django.db import models

# Model to represent a product in the inventory
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Model to represent a product with an image in the inventory
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True) # Product picture
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name