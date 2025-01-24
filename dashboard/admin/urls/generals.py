from django.urls import path,include
from .. import views

urlpatterns = [
    path("",views.AdminDashboardHomeView.as_view(),name="admin-home"),
]