from django.urls import path
from .. import views


urlpatterns = [
    path("order/list/",views.AdminOrderListView.as_view(),name="order-list"),
    path("order/detail/<int:pk>/",views.AdminOrderDetailView.as_view(),name="order-detail"),
    path("order/invoice/<int:pk>/",views.AdminOrderInvoiceView.as_view(),name="order-invoice"),
]