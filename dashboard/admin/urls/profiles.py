from django.urls import path,include
from .. import views



urlpatterns = [
    
    path("security-edit/",views.AdminSecurityEditView.as_view(),name="admin-security-edit"),
    path('profile-edit/',views.AdminProfileEditView.as_view(),name="admin-profile-edit"),
    path('profile-edit-avatar/',views.AdminEditAvatarView.as_view(),name="admin-edit-avatar"),
]