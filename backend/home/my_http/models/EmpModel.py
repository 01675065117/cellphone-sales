import random
from django.db import models
import string


def generate_unique_id():
    length = 6
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k = length))
        if Employee.objects.filter(code = code).count() == 0:
            break
    return code

# Create your models here.
class Employee(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)