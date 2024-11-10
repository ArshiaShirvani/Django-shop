from django.db import models

class CartModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class CartItemsModel(models.Model):
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE)
    product = models.ForeignKey("shop.ProductModel",on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)