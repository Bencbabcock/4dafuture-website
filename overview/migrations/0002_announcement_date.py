# Generated by Django 3.1.7 on 2021-03-03 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]