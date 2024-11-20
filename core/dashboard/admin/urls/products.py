from django.urls import path, include
from .. import views

urlpatterns = [
    path("products-list/",views.AdminProductsListView.as_view(),name="admin-products-list"),
    path("product/edit/<int:pk>/",views.AdminProductEditView.as_view(),name="admin-product-edit"),
    path("product/delete/<int:pk>/",views.AdminProductDeleteView.as_view(),name="admin-product-delete"),
    path("product/create/",views.AdminProductCreateView.as_view(),name="admin-product-create"),
]