from django.shortcuts import render
from .models import ReviewModel,ReviewStatusType
from .forms import SubmitReviewForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class SubmitReviewView(LoginRequiredMixin,CreateView):
    http_method_names = ["post"]    
    model = ReviewModel
    form_class = SubmitReviewForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        
        product = form.cleaned_data['product']
        messages.success(
            self.request,"دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش خواهد شد"
        )
        return redirect(reverse_lazy('shop:product-detail',kwargs={"slug":product.slug}))
        
        
        
        
        
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request,error)
        return redirect(self.request.META.get('HTTP_REFERER'))