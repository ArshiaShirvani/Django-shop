from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('register',views.register_view,name='register'),
    path('complete-profile',views.complete_profile_view,name='complete-profile'),
]