from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("login", views.login_view, name="login"),
     path("logout", views.logout_view, name="logout"),
     path("register/<str:user_selection>", views.register, name="register"),
     path("user-selection", views.select, name="select"),
     path("next-steps/doctor", views.next_steps, name="next"),
]