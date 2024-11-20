from django.urls import path, include
from .. import views

urlpatterns = [
    path("products-list/",views.AdminProductsListView.as_view(),name="admin-products-list"),
]