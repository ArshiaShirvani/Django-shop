from django.contrib import admin
from .models import ContactUsModel,NewsletterModel


@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','content','created_date','seen')

@admin.register(NewsletterModel)
class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ('email','created_date','seen')

