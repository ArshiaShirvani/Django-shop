from django import forms
from .models import ContactUsModel,NewsletterModel

class ContactUsModelForm(forms.ModelForm):
    
    class Meta:
        model = ContactUsModel
        fields = ('first_name','last_name','email','phone_number','content',)

class NewletterModelForm(forms.ModelForm):

    class Meta:
        model = NewsletterModel
        fields = ('email',)