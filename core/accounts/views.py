from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm
from django.contrib import messages

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(
            self.request, 'خوش امدید ❤️')
        return super().form_valid(form)

class LogoutView(auth_views.LogoutView):
    pass
