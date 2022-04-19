from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.Register.as_view(), name="register"),
    path('user/<username>', views.profile, name="profile"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('donor/new/', views.Donor_Create.as_view(), name="new_user"),
    path('recipient/<username>/new/', views.recipient_create, name="new_user"),
    path('user/<username>/payment', views.payment, name="payment")
]