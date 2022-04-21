from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('home/', views.Logged_Home.as_view(), name="logged_home"),
    path('about/', views.About.as_view(), name="about"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.Register.as_view(), name="register"),
    path('user/<username>', views.profile, name="profile"),
    path('user/<int:pk>/delete', views.User_Delete.as_view(), name="user_delete"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('donor/new/', views.Donor_Create.as_view(), name="new_user"),
    path('donor/<int:pk>/update', views.Donor_Update.as_view(), name="donor_update"),
    path('recipient/<username>/new/', views.recipient_create, name="new_user"),
    path('user/<username>/payment', views.payment, name="payment"),
    path('user/<username>/payment/update/<donation>', views.payment_update, name="payment_update")
]