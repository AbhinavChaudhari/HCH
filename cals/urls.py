from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutProject/', views.aboutProject, name='aboutProject'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),

    path('DoctorIndex/',views.DoctorIndex,name='DoctorIndex'),
    path('DoctorLogin/',views.DoctorLogin,name='DoctorLogin'),
    path('DoctorNewPatient/',views.DoctorNewPatient,name='DoctorNewPatient'),
    path('DoctorCalculate/<pid>/', views.DoctorCalculate2, name='DoctorCalculate2'),
    path('addPrescription/<pid>/',views.addPrescription,name='addPrescription'),
    path('addTest/<pid>/',views.addTest,name='addTest'),
    path('addTest2/',views.addTest2,name='addTest2'),
    path('DoctorCalculate/', views.DoctorCalculate, name='DoctorCalculate'),
    path('DoctorPatientViewAll/',views.DoctorPatientViewAll,name='DoctorPatientViewAll'),
    path('DoctorPrescription/',views.DoctorPrescription,name='DoctorPrescription'),
    path('DoctorPrecaution/',views.DoctorPrecaution,name='DoctorPrecaution'),
    path('DoctorSymptom/',views.DoctorSymptom,name='DoctorSymptom'),
    path('DoctorDiet/',views.DoctorDiet,name='DoctorDiet'),
    path('DoctorExercise/',views.DoctorExercise,name='DoctorExercise'),
    path('DoctorLabTestResult/',views.DoctorLabTestResult,name='DoctorLabTestResult'),
    path('DoctorSessionLogout/',views.DoctorSessionLogout,name='DoctorSessionLogout'),
    path('DoctorProceess/',views.DoctorProcess,name='DoctorProcess'),
    path('DoctorProcessP2/',views.DoctorProcessP2,name='DoctorProcessP2'),
    path('DoctorReport/<pid>/',views.DoctorReport,name='DoctorReport'),

    path('PatientIndex', views.PatientIndex, name='PatientIndex'),
    path('PatientIndex2',views.PatientIndex2,name='PatientIndex2'),
    path('PatientLogin/', views.PatientLogin, name='PatientLogin'),
    path('PatientRegister/', views.PatientRegister, name='PatientRegister'),
    path('PatientUpdate/', views.PatientUpdate, name='PatientUpdate'),
    path('PatientDelete/', views.PatientDelete, name='PatientDelete'),
    path('PatientStatusUpdate/', views.PatientStatusUpdate, name='PatientStatusUpdate'),
    path('PatientOldReport/', views.PatientOldReport, name='PatientOldReport'),
    path('PatientSessionLogout',views.PatientSessionLogout,name='PatientSessionLogout'),
    path('PatientCalculate/<pid>/', views.PatientCalculate, name='PatientCalculate2'),
    path('PatientProcess/',views.PatientProcess,name='PatientProcess'),
    path('PatientReport/<pid>/',views.preport),

    path('ReceptionIndex', views.ReceptionIndex, name='ReceptionIndex'),
    path('ReceptionLogin/', views.ReceptionLogin, name='ReceptionLogin'),
    path('ReceptionAddNew/',views.ReceptionAddNew,name='ReceptionAddNew'),
    path('ReceptionPatientViewAll/',views.ReceptionPatientViewAll,name='ReceptionPatientViewAll'),
    path('ReceptionUpdate/', views.ReceptionUpdate, name='ReceptionUpdate'),
    path('ReceptionDelete/', views.ReceptionDelete, name='ReceptionDelete'),
    path('ReceptionStatusUpdate/', views.ReceptionStatusUpdate, name='ReceptionStatusUpdate'),
    path('ReceptionCalculate/<pid>/',views.ReceptionCalculate, name='ReceptionCalculate'),
    path('ReceptionSessionLogout/', views.ReceptionSessionLogout, name='ReceptionSessionLogout'),
    path('ReceptionProcess/',views.ReceptionProcess,name='ReceptionProcess'),



]
