# Generated by Django 2.0.8 on 2018-09-03 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exer3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='Class',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='SName',
            new_name='student',
        ),
    ]
