from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator 

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
    brief_description = models.TextField(null=True,blank=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    discount_percent = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(80)])
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.disabled.value)

    avg_rate = models.FloatField(default=0.0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)

    def get_show_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return '{:,}'.format(round(discounted_amount))
    
    def get_show_raw_price(self):
        return round(self.price)
    
    def is_discounted(self):
        return self.discount_percent != 0
    
    def is_active(self):
        return self.status == ProductStatusType.active.value
    
    def get_price_admin_panel(self):
        return '{:,}'.format(self.price)

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name="product_images")
    file = models.ImageField(upload_to="shop/extra-img/")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class WishListModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)    
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.title