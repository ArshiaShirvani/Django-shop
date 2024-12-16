from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from blog.models import PostModel,PostStatusType,PostCategory
from django.core.exceptions import FieldError

class BlogPostListView(ListView):
    template_name = "blog/post-list.html"
    paginate_by = 3
    context_object_name = 'posts'
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = PostModel.objects.filter(
            status=PostStatusType.active.value)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if category_id := self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        context["categories"] = PostCategory.objects.all()
        return context

class BlogPostDetailView(DetailView):
    template_name = "blog/post-single.html"
    queryset = PostModel.objects.filter(status=PostStatusType.active.value)