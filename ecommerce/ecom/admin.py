from django.contrib import admin
from .models import Customer,Category,Product,Orders,Review
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)