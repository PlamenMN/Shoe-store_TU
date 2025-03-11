from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="shoe_images/")
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
