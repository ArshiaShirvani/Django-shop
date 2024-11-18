from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
class AdminPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        "password_incorrect": _(
            "پسورد فعلی شما اشتباه است  دوباره تلاش کنید"
        ),
        "password_mismatch": _("پسورد های جایگزین شما اشتباه است دوباره تلاش کنید"),
    }