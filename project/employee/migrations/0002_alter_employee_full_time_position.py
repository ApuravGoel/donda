# Generated by Django 4.2.6 on 2023-10-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='full_time_position',
            field=models.CharField(verbose_name='full_time_position'),
        ),
    ]
