from django.urls import path
from .. import views


urlpatterns = [
    path("order-list/",views.CustomerOrderListView.as_view(),name="customer-order-list"),
    path("order/detail/<int:pk>/",views.CustomerOrderDetailView.as_view(),name="customer-order-detail"),
    path("order/invoice/<int:pk>/",views.CustomerOrderInvoiceView.as_view(),name="customer-order-invoice"),
]