# Generated by Django 4.0.6 on 2023-01-02 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0017_alter_doctor_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
