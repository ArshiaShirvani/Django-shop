from django.db import models
from decimal import Decimal

class ProductStatusType(models.IntegerChoices):
    active = 1,("فعال")
    disabled = 2,("غیرفعال")


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode = True,unique=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode = True,unique=True)
    category = models.ManyToManyField(ProductCategoryModel)
    image = models.ImageField(default="shop/default-image/default-product.png",upload_to="shop/upload-image/")
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    discount_percent = models.IntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.disabled.value)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_show_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return '{:,}'.format(round(discounted_amount))

class ProductImageModel(models.Model):
    Product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    file = models.ImageField(default="shop/default-image/default-product.png",upload_to="shop/extra-img/")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)