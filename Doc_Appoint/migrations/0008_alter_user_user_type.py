# Generated by Django 4.0.6 on 2022-12-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0007_rename_user_doctor_doctor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('PR', 'personal'), ('DR', 'doctor')], max_length=2),
        ),
    ]
