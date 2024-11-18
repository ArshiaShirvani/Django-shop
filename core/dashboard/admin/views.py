from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_view
from dashboard.admin.forms import AdminPasswordChangeForm,AdminProfileEditForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from accounts.models import Profile

class AdminDashboardHomeView(LoginRequiredMixin,HasAdminAccessPermission,TemplateView):
    template_name = "dashboard/admin/home.html"
    
class AdminSecurityEditView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,auth_view.PasswordChangeView):
    
    template_name = "dashboard/admin/profile/security-edit.html"
    form_class = AdminPasswordChangeForm
    success_message = "رمز عبور شما با موفقیت تغییر کرد"
    success_url = reverse_lazy("dashboard:admin:admin-security-edit")
    

class AdminProfileEditView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    
    template_name = "dashboard/admin/profile/profile-edit.html"
    form_class = AdminProfileEditForm
    success_message = "پروفایل به روزرسانی شد"
    success_url = reverse_lazy("dashboard:admin:admin-profile-edit")
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    