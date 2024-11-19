from django.urls import path,include
from .. import views


urlpatterns = [
    
    path("",views.CustomerDashboardHomeView.as_view(),name="customer-home"),
    
]