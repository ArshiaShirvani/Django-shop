from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy

class AdminDashboardHomeView(LoginRequiredMixin,HasAdminAccessPermission,TemplateView):
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/home.html"