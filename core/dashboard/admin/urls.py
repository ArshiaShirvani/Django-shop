from django.urls import path,include
from . import views

app_name = "admin"

urlpatterns = [
    path("",views.AdminDashboardHomeView.as_view(),name="admin-home"),
    path("security-edit/",views.AdminSecurityEditView.as_view(),name="admin-security-edit"),
    path('profile-edit/',views.AdminProfileEditView.as_view(),name="admin-profile-edit"),
]