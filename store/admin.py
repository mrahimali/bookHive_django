from django.contrib import admin
from .models import Category, BookInfo, UserDetail, ShippingAddresses, Order, OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Category, CategoryAdmin)





class BookInfoAdmin(admin.ModelAdmin):
    list_display=['title', 'price','writer', 'category', 'uploaded_by' ]


admin.site.register(BookInfo, BookInfoAdmin)




class UserDetailAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'phone']

admin.site.register(UserDetail, UserDetailAdmin)



class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=['address']

admin.site.register(ShippingAddresses, ShippingAddressAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display=['ordered_by']

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order', 'product_owner', 'quantity', 'price']
admin.site.register(OrderItem, OrderItemAdmin)