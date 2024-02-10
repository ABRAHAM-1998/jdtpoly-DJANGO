# compEng/urls.py
from django.urls import path
from . import views

app_name = "compEng"

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("", views.landing_view, name="landing"),
    path("home/", views.home_view, name="home"),
    path("registered-users/", views.registered_users_view, name="registered_users"),
    path("delete_mark/<int:mark_id>/", views.delete_mark_view, name="delete_mark"),
    path("update_mark/<int:mark_id>/", views.update_mark_view, name="update_mark"),
    path("logout/", views.logout_view, name="logout"),
]
