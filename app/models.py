from django.db import models
from django.contrib.auth.models import User




class Userstamp(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_user", related_query_name="%(app_label)s_%(class)ss", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_updated_user", related_query_name="%(app_label)s_%(class)ss", on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True




class Product(Userstamp, Timestamp):
    title = models.CharField(max_length=70)
    quantity = models.PositiveIntegerField(help_text='KGs')
    price = models.PositiveIntegerField()

class Order(Userstamp, Timestamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

