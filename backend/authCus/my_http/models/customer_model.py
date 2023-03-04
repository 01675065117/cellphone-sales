from django.db import models
from django.contrib.auth.hashers import make_password
class Customer(models.Model):
    class Meta:
        db_table = 'customer'
    
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    cus_code = models.CharField(max_length=8, default="", unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    birth = models.DateTimeField()
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Customer, self).save(*args, **kwargs)






