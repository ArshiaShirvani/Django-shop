from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm,UserRegisterForm
from django.contrib import messages
from django.views .generic import (
    FormView,
    CreateView,
    UpdateView)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,get_object_or_404,render
from django.contrib.auth import get_user_model
from accounts.models import Profile,User
from django.http import HttpResponseRedirect



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
    success_url = reverse_lazy("accounts:complete-profile")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            user = authenticate(email=self.request.POST["email"],password=self.request.POST["password1"])
            login(self.request,user)
            messages.success(
            self.request, 'با موفقیت ثبت نام شدید')
        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.POST["password1"] != self.request.POST["password2"]:
            messages.success(
            self.request, 'رمزعبور های شما با یکدیگر مطابقت ندارند')
        else:
            user = User.objects.filter(email = self.request.POST["email"])
            if user is not None:
                messages.success(
                self.request, 'شما قبلا ثبت نام کرده اید')
        return super().form_invalid(form)   

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("website:index")
        return super(SignUpView, self).get(*args, **kwargs)
    
    
def complete_profile_view(request):
    if request.user.is_authenticated:
       
        user = get_object_or_404(Profile,user_id=request.user.id)
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.save()
            messages.success(
                request,"پروفایل شما با موفقیت تکمیل شد"
            )
            return HttpResponseRedirect(reverse_lazy("website:index"))
        else:
            return render(request,'accounts/complete-register.html')
    else:
        return HttpResponseRedirect(reverse_lazy("accounts:register"))
    

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    messages.success(request, 'با موفقیت ثبت نام شدید')
                    login(request,user)
                    return HttpResponseRedirect(reverse_lazy("accounts:complete-profile"))
            else:
                if request.POST["password1"] != request.POST["password2"]:
                    messages.success(request, 'رمزعبور های شما با یکدیگر مطابقت ندارند')
                else:
                    user = User.objects.filter(email = request.POST["email"])
                    if user is not None:
                        messages.success(request, 'شما قبلا ثبت نام کرده اید')           
        form=UserRegisterForm()
        return render(request,'accounts/register.html')
    else:
        return HttpResponseRedirect(reverse_lazy("website:index"))
    
    
class LogoutView(auth_views.LogoutView):
    pass


