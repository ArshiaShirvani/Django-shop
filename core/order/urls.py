from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("validate-coupon/",views.ValidateCouponView.as_view(),name="validate-coupon"),
    path("checkout/",views.OrderCheckOutView.as_view(),name="order-checkout"),
    path("completed/",views.OrderCompletedView.as_view(),name="order-completed"),
]