# Generated by Django 4.1.3 on 2022-12-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr_shahida', '0005_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='featured_image'),
        ),
    ]