# Generated by Django 4.1.3 on 2023-01-15 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dr_shahida', '0009_delete_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
    ]
