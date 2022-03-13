from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("forgot/", views.forgot_view, name="forgot"),
    path("reset/", views.reset_view, name="reset"),
    path("change/", views.change_view, name="change")
]
