from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from django.urls import reverse_lazy

class CustomerDashboardHomeView(LoginRequiredMixin,HasCustomerAccessPermission,TemplateView):
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/customer/home.html"
    
    
