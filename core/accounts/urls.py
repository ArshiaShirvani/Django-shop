from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    # path('register',views.RegisterView.as_view(),name='index'),
    # path('logout',views.LogoutView.as_view(),name='index'),
]