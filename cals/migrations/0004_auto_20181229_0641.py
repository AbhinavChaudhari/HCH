# Generated by Django 2.1.4 on 2018-12-29 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cals', '0003_auto_20181229_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reception',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
