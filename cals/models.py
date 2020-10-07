from django.utils import timezone
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=128)
    contact = models.TextField(max_length=32)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    added_date = models.DateTimeField(default=timezone.now)

class patient(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField(max_length=255)
    contact = models.TextField(max_length=32)
    bloodgroup = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    weight = models.IntegerField()
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    status = models.CharField(max_length=25)
    added_date = models.DateTimeField(default=timezone.now)

class Reception(models.Model):
    name = models.CharField(max_length=128)
    contact = models.TextField(max_length=32)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    added_date = models.DateTimeField(default=timezone.now)

class Symptoms(models.Model):
    Symptom = models.TextField(max_length=32)


class DEP(models.Model):
    disease = models.TextField()
    diet = models.TextField()
    exercise = models.TextField()
    precaution = models.TextField()
    rtest = models.TextField()

class Prescriptions(models.Model):
    pid = models.TextField()
    prescription = models.TextField()
    before = models.TextField()
    after = models.TextField()
    morning = models.TextField()
    afternoon = models.TextField()
    evening = models.TextField()
    days= models.TextField()

class MTest(models.Model):
    pid = models.TextField()
    testname = models.TextField()
    normal_range = models.TextField()
    test_found = models.TextField()
    remark = models.TextField()