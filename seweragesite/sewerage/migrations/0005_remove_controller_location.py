# Generated by Django 3.0.6 on 2020-05-18 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sewerage', '0004_auto_20200517_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controller',
            name='location',
        ),
    ]