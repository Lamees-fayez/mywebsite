from django.contrib import admin
from .models import Product,Car,Employee,Category,User,Login
# Register your models here.
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Login)