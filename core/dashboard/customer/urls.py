from django.urls import path,include
from . import views

app_name = "customer"

urlpatterns = [
    path("",views.CustomerDashboardHomeView.as_view(),name="customer-home"),
]