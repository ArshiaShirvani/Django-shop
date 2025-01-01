from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator 

class OrderStatusType(models.IntegerChoices):
    pending = 1 , "در انتظار پرداخت"
    success = 2, "موفقیت آمیز"
    failed = 3,"لغو شده"

class UserAddressModel(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class CouponModel(models.Model):
    code = models.CharField(max_length=100)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(70)])
    max_limit_usage = models.PositiveIntegerField(default=10)
    used_by = models.ManyToManyField('accounts.User',related_name="coupon_users",blank=True)
    
    expiration_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
    
class OrderModel(models.Model):
    user = models.ForeignKey('accounts.User',on_delete=models.PROTECT)
    
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    
    payment = models.ForeignKey('payment.PaymentModel',on_delete=models.SET_NULL,null=True,blank=True)
    
    total_price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    
    coupon = models.ForeignKey(CouponModel,on_delete=models.PROTECT,null=True,blank=True)
    status = models.IntegerField(choices=OrderStatusType.choices,default=OrderStatusType.pending.value)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())
    
    
    def get_price(self):
        
        if self.coupon:            
            return round(self.total_price - (self.total_price * Decimal( self.coupon.discount_percent /100)))
        else:
            return self.total_price
    
    def __str__(self):
        return self.user.email
    
class OrderItemsModel(models.Model):
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey('shop.ProductModel',on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.title} - {self.order.id}"