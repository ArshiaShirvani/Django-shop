from django.urls import path,include
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact-us/',views.ContactView.as_view(),name='contact'),
    path('submit/ticket/',views.SendTicketView.as_view(),name='send-ticket'),
    path('newsletter/',views.NewletterView.as_view(),name='newsletter'),
]