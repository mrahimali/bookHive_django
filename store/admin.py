from django.contrib import admin
from .models import Category, BookInfo, UserDetail, ShippingAddresses

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Category, CategoryAdmin)





class BookInfoAdmin(admin.ModelAdmin):
    list_display=['title', 'price','writer', 'category' ]


admin.site.register(BookInfo, BookInfoAdmin)




class UserDetailAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'phone']

admin.site.register(UserDetail, UserDetailAdmin)



class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=['address']

admin.site.register(ShippingAddresses, ShippingAddressAdmin)