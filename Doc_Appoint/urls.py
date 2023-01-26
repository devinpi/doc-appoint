from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("login", views.login_view, name="login"),
     path("logout", views.logout_view, name="logout"),
     path("register/<str:user_selection>", views.register, name="register"),
     path("user-selection", views.select, name="select"),
     path("next-steps/doctor", views.next_steps_doc, name="next"),
     path("next-steps/personal", views.next_steps_personal, name="next-personal"),
     path("dashboard-doctor", views.dashboard_doc, name="dashboard-doctor"),
     path("dashboard-personal", views.dashboard_personal, name="dashboard-personal"),
     path("<int:doc_id>", views.book_appointment, name="book-appointment"),
     path("patient_report/<int:p_id>", views.patient_report, name="patient_report"),
     # api routes
     path("dashboard/<str:appointment>", views.get_appointment, name="appoints"),
     path("appointments/<int:doc_id>/<str:selected_date>", views.check_appointment_time, name="check-time"),
     path("dashboard/report/<int:app_id>", views.appointment_report, name="app-report")
]