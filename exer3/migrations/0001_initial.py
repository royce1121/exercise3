# Generated by Django 2.0.8 on 2018-09-03 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(default='SOME STRING', max_length=128)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='members',
            field=models.ManyToManyField(through='exer3.Enrollment', to='exer3.Student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='Class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exer3.Section'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='SName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exer3.Student'),
        ),
    ]
