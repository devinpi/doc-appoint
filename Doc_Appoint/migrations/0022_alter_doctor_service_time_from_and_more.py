# Generated by Django 4.0.6 on 2023-01-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0021_alter_doctor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='service_time_from',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='service_time_to',
            field=models.TimeField(null=True),
        ),
    ]
