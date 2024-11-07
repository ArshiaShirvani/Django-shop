from django.urls import path,include,re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('product-list/',views.ProductListView.as_view(),name='product-list'),
    re_path(r"product/detail/(?P<slug>[-\w]+)/",views.ProductDetailView.as_view(),name="product-detail"),
]