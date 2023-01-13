# Generated by Django 4.0.6 on 2023-01-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0010_alter_doctor_address_alter_doctor_study'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='service_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='service_time_from',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='service_time_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]