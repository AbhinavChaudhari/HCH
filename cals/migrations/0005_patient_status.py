# Generated by Django 2.1.4 on 2018-12-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cals', '0004_auto_20181229_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(default='Pending', max_length=25),
            preserve_default=False,
        ),
    ]
