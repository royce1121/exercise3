# Generated by Django 2.0.8 on 2018-09-03 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exer3', '0002_auto_20180904_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthday',
        ),
    ]
