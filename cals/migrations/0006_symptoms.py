# Generated by Django 2.1.4 on 2019-02-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cals', '0005_patient_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symptom', models.TextField(max_length=32)),
            ],
        ),
    ]
