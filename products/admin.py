from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock","image")
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ("name","image")
class CartAdmin(admin.ModelAdmin):
    list_display = ("user","product","date_added","total")
admin.site.register(models.product,ProductAdmin)
admin.site.register(models.siteimage,SiteImageAdmin)
admin.site.register(models.cart,CartAdmin)