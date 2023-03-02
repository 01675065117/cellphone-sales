import random
from django.db import models
import string

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=8, default="", unique=True)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name