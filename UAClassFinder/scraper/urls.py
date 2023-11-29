from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("change_email/", views.change_email, name="change_email"),
]