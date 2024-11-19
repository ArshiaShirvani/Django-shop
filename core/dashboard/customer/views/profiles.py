from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from ..forms import CustomerPasswordChangeForm,CustomerProfileEditForm
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profile
from django.contrib import messages
from django.shortcuts import redirect

    
class CustomerSecurityEditView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,auth_view.PasswordChangeView):
    template_name = "dashboard/customer/profile/security-edit.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:customer:customer-security-edit")
    success_message = "رمز عبور جدید شما با موفقیت برورزسانی شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user = self.request.user)
    
class CustomerProfileEditView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/customer/profile/profile-edit.html"
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:customer:customer-profile-edit")
    success_message = "پروفایل شما با موفقیت بروزرسانی شد"
    
    def form_invalid(self, form):
        messages.error(self.request,"به روزرسانی پروفایل با مشکل مواجه شد")
        return redirect(self.success_url)
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user = self.request.user)
    

class CustomerAvatarEditView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names = ["post"]
    model = Profile
    success_url = reverse_lazy("dashboard:customer:customer-profile-edit")
    success_message = "به روزرسانی آواتار با موفقیت انجام شد"
    
    fields=[
        "image"
    ]
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user = self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"به روزرسانی آواتار با مشکل مواجه شد")
        return redirect(self.success_url)
    
    
