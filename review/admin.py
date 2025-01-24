from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import ReviewModel


@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','status','created_date')