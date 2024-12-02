from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('register',views.SignUpView.as_view(),name='register'),
]