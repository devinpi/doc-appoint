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
    patient_name = models.ForeignKey('User', on_delete=models.CASCADE, related_name="patient_name")
    report = models.ForeignKey('Report', blank=True, null=True , on_delete=models.CASCADE, related_name="patient_reports")
    
    def __str__(self):
        return f"{self.id} | {self.user} | {self.report}"

class Doctor(models.Model):
    doctor_name = models.ForeignKey('User', on_delete=models.CASCADE, related_name="doctor_name")
    services = models.CharField(max_length=100)
    experience = models.IntegerField()
    study = models.CharField(max_length=100)
    patient = models.ManyToManyField('Patient', blank=True, related_name="doctors_patients", default=0)
    service_time = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.user} | {self.services} | {self.experience} | {self.patient} | {self.service_time} | {self.address}"

class Report(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="report_of_patient")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="report_by_doctor")
    medication = models.TextField(blank=True)
    written_report = models.TextField(blank=True) 
    created_at = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.patient} | {self.doctor} | "