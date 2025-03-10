from django.urls import path
from .. import views

urlpatterns = [
    
    path("coupon/list/",views.AdminCouponListView.as_view(),name="coupon-list"),
    path("coupon/create/",views.AdminCouponCreateView.as_view(),name="coupon-create"),
    path("coupon/edit/<int:pk>/",views.AdminCouponEditView.as_view(),name="coupon-edit"),
    path("coupon/delete/<int:pk>/",views.AdminCouponDeleteView.as_view(),name="coupon-delete"),
    
]