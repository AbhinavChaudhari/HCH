from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'name',
    'contact',
    'email',
    'password',
    'added_date',
   
)

@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'name',
    'contact',
    'email',
    'password',
    'added_date',
   
)

@admin.register(patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'name',
    'contact',
    'email',
    'password',
    'added_date',
   
)

@admin.register(Prescriptions)
class PrescriptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'prescription',
    'before',
    'after',
    'morning',
    'afternoon',
    'evening',
    'days',
   
)

@admin.register(DEP)
class DEPAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'disease',
    'diet',
    'exercise',
    'precaution',
    'rtest',
    
   
)

@admin.register(MTest)
class MTestAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'testname',
    'normal_range',
    'test_found',
    'remark',
    
    
   
)