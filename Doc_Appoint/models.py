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

class Report(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="report_of_patient")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="report_by_doctor")
    medication = models.TextField(blank=True)
    written_report = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.patient} | {self.doctor} | "


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="appoint_patient_name")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="appoint_doctor_name")
    appointment_time = models.CharField(max_length=7, null=True)
    appointment_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.patient} | {self.doctor} | {self.appointment_time} | {self.appointment_date}"

    def serialize(self):
        return {
            # "id": self.id,
            "patient": self.patient.patient_id.id,
            "doctor": self.doctor.doctor_name.id,
            "appointment_time": self.appointment_time,
            "appointment_date": self.appointment_date.strftime("%Y-%m-%d"),
        }

# note: cannot serialize python objects in json. need to change them

