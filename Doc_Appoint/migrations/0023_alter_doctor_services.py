# Generated by Django 4.0.6 on 2023-01-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0022_alter_doctor_service_time_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='services',
            field=models.TextField(max_length=100),
        ),
    ]
