from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ) }
    list_display = ['title', 'price', 'discount_price']

admin.site.register(Item, ItemAdmin)
admin.site.register(Order)

admin.site.register(OrderItem)
