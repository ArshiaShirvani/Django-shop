from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_view
from dashboard.admin.forms import AdminPasswordChangeForm, AdminProfileEditForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from accounts.models import Profile
from django.shortcuts import redirect
from django.core.exceptions import FieldError
from blog.models import PostModel,PostCategory,PostStatusType
from ..forms import BlogForm
from khayyam import JalaliDate

class AdminBlogListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/blog/blog-list.html"
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = PostModel.objects.all()
        
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
    
    def to_jalali(value):
        return JalaliDate(value).strftime('%Y/%m/%d')
    
class AdminBlogEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/blog/blog-edit.html"
    queryset = PostModel.objects.all()
    form_class = BlogForm
    success_message = "ویرایش پست با موفقیت انجام شد"
    
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:admin-blog-edit",kwargs={"pk":self.get_object().pk})
    
class AdminBlogDeleteView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,DeleteView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/blog/blog-delete.html"
    queryset = PostModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:admin-blog-list")
    success_message = "پست با موفقیت حذف شد"
    
class AdminBlogCreateView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,CreateView):
    
    login_url = reverse_lazy('accounts:login')
    template_name = "dashboard/admin/blog/blog-create.html"
    queryset = PostModel.objects.all()
    form_class = BlogForm
    success_message = "پست با موفقیت ایجاد شد"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:admin-blog-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:admin-blog-list")
    
   