from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile

class AdminPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        "password_incorrect": _(
            "پسورد فعلی شما اشتباه است  دوباره تلاش کنید"
        ),
        "password_mismatch": _("پسورد های جایگزین شما اشتباه است دوباره تلاش کنید"),
    }
    
class AdminProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "phone_number",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد نمایید'
        self.fields['last_name'].widget.attrs['class'] = 'form-control '
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی را وارد نمایید'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control text-center'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره همراه را وارد نمایید'
    