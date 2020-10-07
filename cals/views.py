from django.shortcuts import render, get_object_or_404, redirect

from .models import *
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB

# Create your views here.


def DoctorNewPatient(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            all_patients = patient.objects.all()
            checker = 0
            for pname in all_patients:
                if pname.email == request.POST['email']:
                    checker = 1

            if checker == 0:
                p = patient()
                p.name = request.POST['name']
                p.address = request.POST['address']
                p.contact = request.POST['contact']
                p.bloodgroup = request.POST['bloodgroup']
                p.gender = request.POST['gender']
                p.weight = request.POST['weight']
                p.age = request.POST['age']
                p.email = request.POST['email']
                p.password = request.POST['password1']
                p.status = 'Pending'
                p.save()
                DoctorSession = request.COOKIES.get('SessionDoctorLogin')
                return redirect('DoctorIndex')
                # daa
            else:
                DoctorSession = request.COOKIES.get('SessionDoctorLogin')
                return render(request, 'cals/Doctor/DoctorNewPatient.html', {'DS':DoctorSession,'error': 'Email Already Exists.'})
        else:
            DoctorSession = request.COOKIES.get('SessionDoctorLogin')
            return render(request, 'cals/Doctor/DoctorNewPatient.html', {'DS':DoctorSession,'error': 'Password doesn\'t matched'})
    else:
        all_patient_all = patient.objects.all()
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorNewPatient.html',{'patients': all_patient_all,'DS':DoctorSession})

def DoctorLogin(request):
    if request.method == 'POST':
        all_doctor = Doctor.objects.all()
        checker = 0
        for dr in all_doctor:
            if dr.email == request.POST['email'] and dr.password == request.POST['password']:
                checker = 1

        if checker == 1:
            all_patient_all = patient.objects.all()
            DoctorSession = request.COOKIES.get('SessionDoctorLogin')
            response = render(request,'cals/Doctor/DoctorDashboard.html',{'patients': all_patient_all,'DS':DoctorSession})
            response.set_cookie('SessionDoctorLogin', request.POST['email'])
            return response
        else:
            DoctorSession = request.COOKIES.get('SessionDoctorLogin')
            return render(request, 'cals/Doctor/DoctorLogin.html', {'error': 'Please check Email and Password.','DS':DoctorSession})

    else:
        return render(request,'cals/Doctor/DoctorLogin.html')


def DoctorIndex(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        all_patient_all  = patient.objects.all()
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorDashboard.html', {'patients': all_patient_all,'DS':DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorLogin.html')

def DoctorCalculate2(request,pid):
    DoctorSession = request.COOKIES.get('SessionDoctorLogin')
    #getting Patient Data
    patient2 = patient.objects.get(id=pid)
    return render(request,'cals/Doctor/DoctorCalculate.html',{'DS':DoctorSession,'patient':patient2})

def addPrescription(request,pid):
    DoctorSession = request.COOKIES.get('SessionDoctorLogin')
    patient2 = patient.objects.get(id=pid)
    return render(request, 'cals/Doctor/DoctorPrescription.html', {'DS':DoctorSession,'patient':patient2})


def DoctorCalculate(request):
    DoctorSession = request.COOKIES.get('SessionDoctorLogin')
    #getting Patient Data
    patient2 = patient.objects.get(id=1)
    return render(request,'cals/Doctor/DoctorCalculate.html',{'DS':DoctorSession,'patient':patient2})

def DoctorPatientViewAll(request):
    all_patient_all = patient.objects.all()
    DoctorSession = request.COOKIES.get('SessionDoctorLogin')
    return render(request, 'cals/Doctor/DoctorPatientViewAll.html', {'patients': all_patient_all,'DS':DoctorSession})

def DoctorSessionLogout(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        response = redirect('DoctorLogin')
        response.delete_cookie("SessionDoctorLogin")
        return response

def PatientSessionLogout(request):
    if request.COOKIES.get('SessionPatientLogin'):
        response = redirect('PatientLogin')
        response.delete_cookie("SessionPatientLogin")
        return response

def ReceptionSessionLogout(request):
    if request.COOKIES.get('SessionReceptionLogin'):
        response = redirect('ReceptionLogin')
        response.delete_cookie("SessionReceptionLogin")
        return response

def index(request):
    return render(request,'cals/Home/index.html')

def aboutProject(request):
    return render(request,'cals/Home/aboutProject.html')

def aboutUs(request):
    return render(request,'cals/Home/aboutUs.html')

def PatientRegister(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            all_patients = patient.objects.all()
            checker = 0
            for pname in all_patients:
                if pname.email == request.POST['email']:
                    checker = 1

            if checker == 0:
                p = patient()
                p.name = request.POST['name']
                p.address = request.POST['address']
                p.contact = request.POST['contact']
                p.bloodgroup = request.POST['bloodgroup']
                p.gender = request.POST['gender']
                p.weight = request.POST['weight']
                p.age = request.POST['age']
                p.email = request.POST['email']
                p.password = request.POST['password1']
                p.status = 'Pending'
                p.save()
                return redirect('PatientLogin')
                # daa
            else:
                return render(request, 'cals/Patient/PatientRegister.html', {'error': 'Email Already Exists.'})
        else:
            return render(request, 'cals/Patient/PatientRegister.html', {'error': 'Password doesn\'t matched'})

    else:
        return render(request, 'cals/Patient/PatientRegister.html')


def PatientLogin(request):
    if request.method == 'POST':
        if request.POST['email'] and request.POST['password']:
            all_patients = patient.objects.all()
            checker = 0
            for pname in all_patients:
                if pname.email == request.POST['email'] and pname.password == request.POST['password']:
                    checker = 1

            if checker == 1:
                response = redirect('PatientIndex2')
                response.set_cookie('SessionPatientLogin', request.POST['email'])
                return response
            else:
                PatientSession = request.COOKIES.get('SessionPatientLogin')
                return render(request, 'cals/Patient/PatientLogin.html', {'PS':PatientSession,'error': 'Please check Email and Password.'})
    else:
        return render(request, 'cals/Patient/PatientLogin.html')


def PatientIndex(request):
    if request.COOKIES.get('SessionPatientLogin'):
        return redirect('PatientIndex')
    else:
        return render(request, 'cals/Patient/PatientLogin.html')

def PatientUpdate(request):
    if request.method == 'POST':
        updateingPatient = get_object_or_404(patient, id=request.POST['PatientId'])
        updateingPatient.name = request.POST['name']
        updateingPatient.address = request.POST['address']
        updateingPatient.contact = request.POST['contact']
        updateingPatient.bloodgroup = request.POST['bloodgroup']
        updateingPatient.gender = request.POST['gender']
        updateingPatient.weight = request.POST['weight']
        updateingPatient.age = request.POST['age']
        updateingPatient.save()
        return redirect('DoctorIndex')

def PatientDelete(request):
    if request.method == 'POST':
        deletePatient = get_object_or_404(patient,id=request.POST['PatientId'])
        deletePatient.delete()
        return redirect('DoctorIndex')

def PatientStatusUpdate(request):
    if request.method == 'POST':
        StatusUpdatingPAtient = get_object_or_404(patient,id=request.POST['PatientId'])
        StatusUpdatingPAtient.status = request.POST['status']
        StatusUpdatingPAtient.save()
        return redirect('DoctorIndex')

def PatientOldReport(request):
    if request.COOKIES.get('SessionPatientLogin'):
        PatientSession = request.COOKIES.get('SessionPatientLogin')
        return render(request, 'cals/Patient/PatientOldReport.html',{'PS':PatientSession})
    else:
        return render(request, 'cals/Patient/PatientLogin.html')

def ReceptionLogin(request):
    if request.method == 'POST':
        all_Reception = Reception.objects.all()
        checker = 0
        for dr in all_Reception:
            if dr.email == request.POST['email'] and dr.password == request.POST['password']:
                checker = 1

        if checker == 1:
            response = render(request,'cals/Reception/ReceptionDashboard.html',{'RS':request.POST['email']})
            response.set_cookie('SessionReceptionLogin', request.POST['email'])
            return response
        else:
            return render(request, 'cals/Reception/ReceptionLogin.html', {'error': 'Please check Email and Password.'})

    else:
        return render(request,'cals/Reception/ReceptionLogin.html')


def ReceptionIndex(request):
    if request.COOKIES.get('SessionReceptionLogin'):
        ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
        return render(request, 'cals/Reception/ReceptionDashboard.html',{'RS':ReceptionSession})
    else:
        return render(request, 'cals/Reception/ReceptionLogin.html')

def ReceptionAddNew(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            all_patients = patient.objects.all()
            checker = 0
            for pname in all_patients:
                if pname.email == request.POST['email']:
                    checker = 1

            if checker == 0:
                p = patient()
                p.name = request.POST['name']
                p.address = request.POST['address']
                p.contact = request.POST['contact']
                p.bloodgroup = request.POST['bloodgroup']
                p.gender = request.POST['gender']
                p.weight = request.POST['weight']
                p.age = request.POST['age']
                p.email = request.POST['email']
                p.password = request.POST['password1']
                p.status = 'Pending'
                p.save()
                return redirect('ReceptionIndex')
                # daa
            else:
                ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
                return render(request, 'cals/Reception/ReceptionAddNew.html', {'RS':ReceptionSession,'error': 'Email Already Exists.'})
        else:
            ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
            return render(request, 'cals/Reception/ReceptionAddNew.html', {'RS':ReceptionSession,'error': 'Password doesn\'t matched'})
    else:
        all_patient_all = patient.objects.all()
        ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
        return render(request, 'cals/Reception/ReceptionAddNew.html',{'RS':ReceptionSession,'patients': all_patient_all})


def ReceptionUpdate(request):
    if request.method == 'POST':
        updateingPatient = get_object_or_404(patient, id=request.POST['PatientId'])
        updateingPatient.name = request.POST['name']
        updateingPatient.address = request.POST['address']
        updateingPatient.contact = request.POST['contact']
        updateingPatient.bloodgroup = request.POST['bloodgroup']
        updateingPatient.gender = request.POST['gender']
        updateingPatient.weight = request.POST['weight']
        updateingPatient.age = request.POST['age']
        updateingPatient.save()
        return redirect('ReceptionIndex')

def ReceptionDelete(request):
    if request.method == 'POST':
        deletePatient = get_object_or_404(patient,id=request.POST['PatientId'])
        deletePatient.delete()
        return redirect('ReceptionIndex')

def ReceptionStatusUpdate(request):
    if request.method == 'POST':
        StatusUpdatingPAtient = get_object_or_404(patient,id=request.POST['PatientId'])
        StatusUpdatingPAtient.status = request.POST['status']
        StatusUpdatingPAtient.save()
        return redirect('ReceptionIndex')

def ReceptionPatientViewAll(request):
    if request.COOKIES.get('SessionReceptionLogin'):
        all_patient_all = patient.objects.all()
        ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
        return render(request, 'cals/Reception/ReceptionPatientViewAll.html',{'RS': ReceptionSession,'patients': all_patient_all})
    else:
        return render(request, 'cals/Reception/ReceptionLogin.html')

def DoctorPrescription(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorPrescription.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorPrescription.html')

def DoctorPrecaution(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorPrecaution.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorPrecaution.html')

def DoctorSymptom(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorSymptom.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorSymptom.html')

def DoctorProcess(request):
    if request.method == 'POST':
        print("Loading Traning.csv")
        df = pd.read_csv('https://vishuamu.github.io/Training.csv')

        X = df.iloc[:, :-1]
        y = df['prognosis']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

        rf_clf = GaussianNB()
        rf_clf.fit(X_train, y_train)

        print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

        symptoms_dict = {}

        for index, symptom in enumerate(X):
            symptoms_dict[symptom] = index

        symptoms_dict

        input_vector = np.zeros(len(symptoms_dict))
        sym = request.POST.getlist('sym')
        symc = []
        for symi in sym:
            symc.append(symptoms_dict[symi])
        input_vector[[symc]] = 1
        rf_clf.predict_proba([input_vector])
        result = rf_clf.predict([input_vector])
        result = result[0]
        # we got Disease
        dep = DEP.objects.get(disease=result)
        diet = dep.diet.split(',')
        exercise = dep.exercise.split(',')
        precaution = dep.precaution.split(',')
        rtest = dep.rtest.split(',')
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        patient2 = patient.objects.get(id=request.POST['did'])
        return render(request, 'cals/Doctor/DoctorCalculate.html', {'DS': DoctorSession, 'patient': patient2,'Disease':result,'diet':diet,'exercise':exercise,'precaution':precaution,'rtest':rtest})

def DoctorProcessP2(request):
    if request.method == "POST":
        p = Prescriptions()
        p.pid = request.POST['pid']
        p.prescription = request.POST['prescription']

        if request.POST['beforeafter'] == 'before':
            p.before = 'before'
        else:
            p.before = ''

        if request.POST['beforeafter'] == 'after':
            p.after = 'after'
        else:
            p.after = ''

        if 'morning' in request.POST:
            p.morning = 'morning'
        else:
            p.morning = ''

        if 'afternoon' in request.POST:
            p.afternoon = request.POST['afternoon']
        else:
            p.afternoon = ''

        if 'evening' in request.POST:
            p.evening = request.POST['evening']
        else:
            p.evening = ''

        p.days = request.POST['days']

        p.save()
        print("patient id : "+request.POST['pid'])
        # print("patient id :"+int(request.POST['pid']))

        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        patient2 = patient.objects.get(id=request.POST['pid'])
        prescription  = Prescriptions.objects.filter(pid = request.POST['pid'])
        return render(request, 'cals/Doctor/DoctorPrescription.html',
                      {'DS': DoctorSession, 'patient': patient2, 'Disease': request.POST['disease'], 'prescription':prescription})
    else:

        return render(request,'cals/Doctor/test.html')

def addTest(request,pid):
    if request.method == "POST":
        p = Prescriptions()
        p.pid = request.POST['pid']
        p.prescription = request.POST['prescription']

        if request.POST['beforeafter'] == 'before':
            p.before = 'before'
        else:
            p.before = ''

        if request.POST['beforeafter'] == 'after':
            p.after = 'after'
        else:
            p.after = ''

        if request.POST['morning']:
            p.morning = 'morning'
        else:
            p.morning = ''

        if request.POST['afternoon']:
            p.afternoon = request.POST['afternoon']
        else:
            p.afternoon = ''

        if request.POST['evening']:
            p.evening = request.POST['evening']
        else:
            p.evening = ''

        p.days = request.POST['days']

        p.save()
        print("patient id : "+request.POST['pid'])
        # print("patient id :"+int(request.POST['pid']))

        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        patient2 = patient.objects.get(id=request.POST['pid'])
        prescription  = Prescriptions.objects.filter(pid = request.POST['pid'])
        return render(request, 'cals/Doctor/DoctorPrescription.html',
                      {'DS': DoctorSession, 'patient': patient2, 'Disease': request.POST['disease'], 'prescription':prescription})
    else:
        patient2 = patient.objects.get(id=pid)
        return render(request,'cals/Doctor/DoctorTest.html',{'patient': patient2})

def addTest2(request):
    if request.method == "POST":
        p = MTest()
        p.pid = request.POST['pid']
        p.testname = request.POST['tests']
        p.normal_range = request.POST['NormalRange']
        p.test_found = request.POST['TestFound']
        p.remark = request.POST['Remark']
        p.save()

        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        patient2 = patient.objects.get(id=request.POST['pid'])
        mTest = MTest.objects.filter(pid=request.POST['pid'])
        return render(request, 'cals/Doctor/DoctorTest.html',
                      {'DS': DoctorSession, 'patient': patient2,
                       'mTest': mTest})
    else:
        return render(request, 'cals/Doctor/DoctorTest.html')

def DoctorReport(request,pid):
    DoctorSession = request.COOKIES.get('SessionDoctorLogin')
    patient2 = patient.objects.get(id=pid)
    mTest = MTest.objects.filter(pid=pid)
    prescription = Prescriptions.objects.filter(pid=pid)
    return render(request, 'cals/Doctor/DoctorReport.html',{'DS': DoctorSession, 'patient': patient2,
                       'mTest': mTest,'prescription':prescription})


def DoctorDiet(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorDiet.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorDiet.html')

def DoctorExercise(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorExercise.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorExercise.html')

def DoctorLabTestResult(request):
    if request.COOKIES.get('SessionDoctorLogin'):
        DoctorSession = request.COOKIES.get('SessionDoctorLogin')
        return render(request, 'cals/Doctor/DoctorLabTestResult.html',{'RS': DoctorSession})
    else:
        return render(request, 'cals/Doctor/DoctorLabTestResult.html')

def PatientIndex2(request):

    PatientSession = request.COOKIES.get('SessionPatientLogin')
    patient2 = patient.objects.get(email=PatientSession)
    return render(request,'cals/Patient/PatientDashboard.html',{'PS':PatientSession,'patient':patient2})

def PatientCalculate(request, pid):
    patient2 = patient.objects.get(id=pid)
    PatientSession = request.COOKIES.get('SessionPatientLogin')
    return render(request,'cals/Patient/Patientcalculate.html',{'PS':PatientSession,'patient': patient2})

def PatientProcess(request):
    if request.method == 'POST':
        print("Loading Traning.csv")
        df = pd.read_csv('https://vishuamu.github.io/Training.csv')

        X = df.iloc[:, :-1]
        y = df['prognosis']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

        rf_clf = GaussianNB()
        rf_clf.fit(X_train, y_train)

        print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

        symptoms_dict = {}

        for index, symptom in enumerate(X):
            symptoms_dict[symptom] = index

        symptoms_dict

        input_vector = np.zeros(len(symptoms_dict))
        sym = request.POST.getlist('sym')
        symc = []
        for symi in sym:
            symc.append(symptoms_dict[symi])
        input_vector[[symc]] = 1
        rf_clf.predict_proba([input_vector])
        result = rf_clf.predict([input_vector])
        result = result[0]
        # we got Disease
        dep = DEP.objects.get(disease=result)
        diet = dep.diet.split(',')
        exercise = dep.exercise.split(',')
        precaution = dep.precaution.split(',')
        rtest = dep.rtest.split(',')
        PatientSession = request.COOKIES.get('SessionPatientLogin')
        patient2 = patient.objects.get(id=request.POST['did'])
        return render(request, 'cals/Patient/Patientcalculate.html', {'PS':PatientSession, 'patient': patient2,'Disease':result,'diet':diet,'exercise':exercise,'precaution':precaution,'rtest':rtest})


def ReceptionCalculate(request,pid):
    if request.COOKIES.get('SessionReceptionLogin'):
        ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
        patient2 = patient.objects.get(id=pid)
        return render(request, 'cals/Reception/ReceptionCalculate.html',{'RS': ReceptionSession,'patient': patient2})
    else:
        return render(request, 'cals/Reception/ReceptionLogin.html')

def ReceptionProcess(request):
    if request.method == 'POST':
        print("Loading Traning.csv")
        df = pd.read_csv('https://vishuamu.github.io/Training.csv')

        X = df.iloc[:, :-1]
        y = df['prognosis']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

        rf_clf = GaussianNB()
        rf_clf.fit(X_train, y_train)

        print("Accuracy on split test: ", rf_clf.score(X_test,y_test))

        symptoms_dict = {}

        for index, symptom in enumerate(X):
            symptoms_dict[symptom] = index

        symptoms_dict

        input_vector = np.zeros(len(symptoms_dict))
        sym = request.POST.getlist('sym')
        symc = []
        for symi in sym:
            symc.append(symptoms_dict[symi])
        input_vector[[symc]] = 1
        rf_clf.predict_proba([input_vector])
        result = rf_clf.predict([input_vector])
        result = result[0]
        # we got Disease
        dep = DEP.objects.get(disease=result)
        diet = dep.diet.split(',')
        exercise = dep.exercise.split(',')
        precaution = dep.precaution.split(',')
        rtest = dep.rtest.split(',')
        ReceptionSession = request.COOKIES.get('SessionReceptionLogin')
        patient2 = patient.objects.get(id=request.POST['did'])
        return render(request, 'cals/Reception/ReceptionCalculate.html', {'RS': ReceptionSession, 'patient': patient2,'Disease':result,'diet':diet,'exercise':exercise,'precaution':precaution,'rtest':rtest})


def preport(request,pid):

    return render(request,'cals/Patient/PatientReport.html')


def preport(request,pid):
    PatientSession = request.COOKIES.get('SessionPatientLogin')
    patient2 = patient.objects.get(id=pid)
    mTest = MTest.objects.filter(pid=pid)
    prescription = Prescriptions.objects.filter(pid=pid)
    return render(request, 'cals/Patient/PatientReport.html', {'PS':PatientSession, 'patient': patient2,
                                                             'mTest': mTest, 'prescription': prescription})