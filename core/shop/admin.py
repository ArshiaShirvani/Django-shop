from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import ProductModel,ProductImageModel,ProductCategoryModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','stock','status','price','created_date',)

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_date',)

@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('id','file','created_date',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

