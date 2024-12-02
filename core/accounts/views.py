from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm,UserRegisterForm
from django.contrib import messages
from django.views .generic import FormView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(
            self.request, 'خوش امدید ❤️')
        return super().form_valid(form)
    

class SignUpView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("website:index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request.user)
            messages.success(
            self.request, 'با موفقیت ثبت نام شدید')
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("website:index")
        return super(SignUpView, self).get(*args, **kwargs)
    
class LogoutView(auth_views.LogoutView):
    pass
