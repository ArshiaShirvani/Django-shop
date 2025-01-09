from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView,
                                  TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from shop.models import WishListModel
from django.core.exceptions import FieldError

class CustomerWishListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):
    template_name = "dashboard/customer/wishlists/wishlist-list.html"
    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = WishListModel.objects.filter(user=self.request.user)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(product__title__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context
    
    
class CustomerWishListDeleteView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,DeleteView):
    
    http_method_names = ["post"]
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/wishlists/wishlist-list.html"
    success_message = "محصول با موفقیت از لیست حذف شد"
    success_url = reverse_lazy("dashboard:customer:wishlist-list")
    
    def get_queryset(self):
        return WishListModel.objects.filter(user=self.request.user)
    
    

    
   