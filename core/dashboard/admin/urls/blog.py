from django.urls import path
from .. import views

urlpatterns = [
    path("post-list/",views.AdminBlogListView.as_view(),name="admin-blog-list"),
    path("post-edit/<int:pk>/",views.AdminBlogEditView.as_view(),name="admin-blog-edit"),
    path("post-delete/<int:pk>/",views.AdminBlogDeleteView.as_view(),name="admin-blog-delete"),
    path("post-create/",views.AdminBlogCreateView.as_view(),name="admin-blog-create"),
    
]