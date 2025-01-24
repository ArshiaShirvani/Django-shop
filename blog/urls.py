from django.urls import path,re_path
from . import views

app_name = "blog"

urlpatterns = [
    path("post-list/",views.BlogPostListView.as_view(),name="post-list"),
    re_path(r"post/detail/(?P<slug>[-\w]+)/",views.BlogPostDetailView.as_view(),name="post-detail"),
]