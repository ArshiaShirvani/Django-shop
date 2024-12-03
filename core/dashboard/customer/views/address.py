from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView,
                                  TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from order.models import UserAddressModel
from ..forms import UserAddressForm

class CustomerAddressListView(LoginRequiredMixin, HasCustomerAccessPermission, ListView):

    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/addresses/address-list.html"

    def get_queryset(self):
        queryset = UserAddressModel.objects.filter(user=self.request.user)
        
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context
    
class CustomerAddressEditView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/addresses/address-edit.html"

    form_class = UserAddressForm
    success_message = "ویرایش آدرس با موفقیت انجام شد"
    
    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy("dashboard:customer:customer-address-edit",kwargs={"pk":self.get_object().pk})
    
class CustomerAddressDeleteView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,DeleteView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/addresses/address-delete.html"

    success_url = reverse_lazy("dashboard:customer:customer-address-list")
    success_message = "آدرس با موفقیت حذف شد"
    
    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
    
class CustomerAddressCreateView(LoginRequiredMixin, HasCustomerAccessPermission,SuccessMessageMixin,CreateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/addresses/address-create.html"

    form_class = UserAddressForm
    success_message = "آدرس با موفقیت اضافه شد"
    
    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:customer:customer-address-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:customer:customer-address-list")
    
   