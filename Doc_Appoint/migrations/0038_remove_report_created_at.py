# Generated by Django 4.0.6 on 2023-01-21 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doc_Appoint', '0037_remove_report_medication_alter_report_written_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='created_at',
        ),
    ]
