from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.permissions import HasCustomerAccessPermission
from . models import UserAddressModel
    
    
class OrderCheckOutView(LoginRequiredMixin,HasCustomerAccessPermission,TemplateView):
    template_name = "order/checkout.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["addresses"] = UserAddressModel.objects.filter(user=self.request.user)
        return context
