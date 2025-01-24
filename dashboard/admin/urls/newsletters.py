from django.urls import path
from .. import views

urlpatterns = [
    path("newsletters-list/",views.AdminNewsLettersListView.as_view(),name="admin-newsletters"),
    path("newsletters/delete/<int:pk>/",views.NewsletterDeleteView.as_view(),name="admin-newsletters-delete")
]