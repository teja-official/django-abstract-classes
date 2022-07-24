from django.contrib import admin

from app.models import Order, Product

admin.site.register(Product)
admin.site.register(Order)