from django.urls import path
from .. import views


urlpatterns = [
    path("address-list/",views.CustomerAddressListView.as_view(),name="customer-address-list"),
    path("address/create/",views.CustomerAddressCreateView.as_view(),name="customer-address-create"),
    path("address/edit/<int:pk>/",views.CustomerAddressEditView.as_view(),name="customer-address-edit"),
    path("address/delete/<int:pk>/",views.CustomerAddressDeleteView.as_view(),name="customer-address-delete"),
]