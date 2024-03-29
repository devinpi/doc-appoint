# Generated by Django 4.0.6 on 2023-01-17 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0027_alter_doctor_service_time_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.TimeField()),
                ('appointment_date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appoint_doctor_name', to='Doc_Appoint.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appoint_patient_name', to='Doc_Appoint.patient')),
            ],
        ),
    ]
