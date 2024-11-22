from django.urls import path,include
from .. import views


urlpatterns = [
    path("user-list/", views.UserListView.as_view(), name="user-list"),
    path("user/delete/<int:pk>/", views.UserDeleteView.as_view(), name="user-delete"),
    path("user/edit/<int:pk>/", views.UserUpdateView.as_view(), name="user-edit"),
]