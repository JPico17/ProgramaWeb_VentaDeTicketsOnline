# Generated by Django 5.0.4 on 2024-11-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_reserva_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='evento',
        ),
    ]
