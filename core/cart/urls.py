from django.urls import path,re_path
from . import views

app_name = "cart"

urlpatterns = [
    path('session/add-product/',views.SessionAddProductView.as_view(),name='session-add-product'),
    path('session/cart/summary/',views.SessionCartSummaryView.as_view(),name='session-cart-summary'),
    path('session/cart/delete-product/',views.SessionDeleteProductView.as_view(),name='session-cart-delete-product'),
    path('session/cart/update-product/',views.SessionUpdateQuantityProductView.as_view(),name='session-cart-update-product'),
]