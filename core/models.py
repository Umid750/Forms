from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    price = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    image = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.name