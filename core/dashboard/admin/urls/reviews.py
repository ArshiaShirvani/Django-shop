from django.urls import path
from .. import views

urlpatterns = [
    path("review/list/",views.AdminReviewListView.as_view(),name="review-list"),
    path("review/edit/<int:pk>/",views.AdminReviewEditView.as_view(),name="review-edit"),
]