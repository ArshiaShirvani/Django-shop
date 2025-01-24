from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import PaymentModel

@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('id','authority_id','ref_id','amount','status','response_code','created_date',)