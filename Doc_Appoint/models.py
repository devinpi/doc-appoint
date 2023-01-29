from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    USER_REGISTER_TYPES = (
        ('PR', 'personal'),
        ('DR', 'doctor')
    )   
    user_type = models.CharField(max_length=2, blank=True, choices=USER_REGISTER_TYPES)

class Patient(models.Model):
    patient_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name="patient_id", default=0)
    full_name = models.CharField(max_length=50, null=True)
    patient_phone_number = models.CharField(max_length=14, blank=True, null=True)
    patient_dob = models.DateField(null=True, blank=True)
    patient_sex = models.CharField(max_length=10, null=True)
    def __str__(self):
        return f"{self.patient_id} | {self.full_name} | {self.patient_dob} | {self.patient_sex}"

    def serialize(self):
        return {
            # "id": self.id,
            "patient_id": self.patient_id.id,
            # "full_name": self.full_name,
            # "patient_dob": self.patient_dob
        }

class Doctor(models.Model):
    doctor_name = models.ForeignKey('User', on_delete=models.CASCADE, related_name="doctor_name")
    services = models.TextField(max_length=100)
    experience = models.IntegerField()
    study = models.TextField()
    patient = models.ManyToManyField('Patient', blank=True, related_name="doctors_patients", default=[0])
    service_time_from = models.TimeField(null=True)
    service_time_to = models.TimeField(null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.id} | {self.services} | {self.experience} | {self.patient} | {self.address}"

    def serialize(self):
        return {
            "id": self.id,
            "doctor": self.doctor_name.username,
            "services": self.services,
            "service_time_from": self.service_time_from,
            "service_time_to": self.service_time_to,
            "phone_number": self.phone_number,
        }

class Report(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="report_of_patient")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="report_by_doctor")
    written_report = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.id} | {self.patient} | {self.doctor} | "

    def serialize(self):
        return {
            "id": self.id,
            "written_report": self.written_report
        }


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="appoint_patient_name")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="appoint_doctor_name")
    report = models.ForeignKey('Report', null=True, blank=True, on_delete=models.CASCADE, related_name="patient_report_by_appointment")
    appointment_time = models.CharField(max_length=10, null=True)
    appointment_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.patient} | {self.doctor} | {self.appointment_time} | {self.appointment_date}"

    def serialize(self):
        return {
            "id": self.id,
            # "patient": self.patient.patient_id.id,
            "patient": self.patient.full_name,
            "doctor": self.doctor.doctor_name.username,
            "report": self.report.written_report,
            "appointment_time": self.appointment_time,
            "appointment_date": self.appointment_date.strftime("%Y-%m-%d"),
        }

# note: cannot serialize python objects in json. need to change them

