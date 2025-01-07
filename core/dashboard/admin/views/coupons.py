from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.core.exceptions import FieldError
from ..forms import CouponForm
from order.models import CouponModel


class AdminCouponListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/coupon/coupon-list.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = CouponModel.objects.all()
        
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(code__icontains=search_q)
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
    
class AdminCouponEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/coupon/coupon-edit.html"
    
    form_class = CouponForm
    success_message = "ویرایش کد تخفیف با موفقیت انجام شد"
    
    def get_queryset(self):
        return CouponModel.objects.all()
    
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-edit",kwargs={"pk":self.get_object().pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AdminCouponDeleteView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,DeleteView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/coupon/coupon-delete.html"
    queryset = CouponModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:coupon-list")
    success_message = "کد نخفیف با موفقیت حذف شد"
    
class AdminCouponCreateView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,CreateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/coupon/coupon-create.html"
    queryset = CouponModel.objects.all()
    form_class = CouponForm
    success_message = "کد تخفیف با موفقیت ایجاد شد"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:coupon-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-list")
    
   