from django.urls import path,include
from .. import views


urlpatterns = [
    
    path("security-edit/",views.CustomerSecurityEditView.as_view(),name="customer-security-edit"),
    path("profile-edit/",views.CustomerProfileEditView.as_view(),name="customer-profile-edit"),
    path("profile-edit-avatar/",views.CustomerAvatarEditView.as_view(),name="customer-avatar-edit"),
    
]