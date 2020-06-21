from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from.models import *
from .forms import *
from .decorators import *

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            Customer.objects.create(
                user=user,name = user.username, phone = None, email = user.email
            )
            messages.success(request, 'Account was created for ' + user.username)
            return redirect('/login')
    context = {'form':form}
    return render(request, 'users/register.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profilePage(request):
	return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
def initiateDatabase(request):
    line = ['Acetaminophen', 'Adenosine', 'Advil', 'Allopurinol', 'Alprazolam', 'Amlodipine', 'Amoxicillin', 'Aspirin', 'Atenolol', 'Azithromycin', 'Bupropion', 'Carvedilol', 'Citalopram', 'Clopidogrel', 'Cyclobenzaprine', 'Duloxetine', 'Escitalopram', 'Fenofibrate', 'Fluoxetine', 'Fluticasone', 'Furosemide', 'Gabapentin', 'Hydrochlorothiazide', 'Hydroxyzine', 'Levothyroxine', 'Liothryonine', 'Lipitor', 'Lisinopril', 'Losartan', 'Meloxicam', 'Metformin', 'Metoprolol', 'Montelukast', 'Naloxone', 'NasonexOmeprazole', 'Pantoprazole', 'Pravastatin', 'Prednisone', 'Sertraline', 'Simvastatin', 'Tamsulosin', 'Tramadol', 'Trazodone', 'Tylenol', 'Venlafaxine', 'Ventolin', 'Vicodin', 'Warfarin', 'Zolpidee']
    for i in range(len(line)):
        Med = Medication(name=line[i])
        Med.save()
    line2 = ['Ache', 'Acne', 'Allergic reaction', 'Amnesia', 'Blindness', 'Bloating', 'Blurry Vision', 'Bruse', 'Chest pain', 'Chills', 'Constipation', 'Cough', 'Depression', 'Diarrhea', 'Dizziness', 'Drowsiness', 'Dry mouth', 'Dry skin', 'Edema', 'Fatigue', 'Fever', 'Hallucination', 'Headache', 'Hearing loss', 'Heartburn', 'Hiccups', 'Hives', 'Insomnia', 'Loss of Appetite', 'Nausea', 'Nervousness', 'Nose bleed', 'Numbness', 'Pneumonia', 'Rash', 'Redness', 'Seizures', 'Shock', 'Slurred speech', 'Stomach pain', 'Stress', 'Stroke', 'Swelling', 'Thirst', 'Tinnitus', 'Tremor', 'Ulcer', 'Vomiting', 'Weight gain', 'Weight loss']
    for i in range(len(line)):
        Symp = SideEffect(name=line[i])
        Symp.save()
    return redirect('/')

def getData(request):
    customer = request.user.customer
    medlogs = customer.medlog_set.all()
    customer_medications = customer.medications.all()
    medlog_data = []
    for cmed in customer_medications:
        med_data = []
        for log in cmed.medication.medlog_set.all():
            med_data.append({str(log.date_created):log.number_of_doses})
        medlog_data.append({cmed.medication.name:med_data})

    slogs = customer.symptomlog_set.all()
    customer_symptoms = customer.my_side_effects_list.all()
    slog_data = []
    for side_effect in customer_symptoms:
        symptom_data = []
        for log in side_effect.symptomlog_set.all():
            symptom_data.append({log.date_created:log.number_of_doses})
        slog_data.append({side_effect:symptom_data})
    graph_data = [{"mdata":medlog_data},{"sdata":slog_data}]
    return JsonResponse(graph_data, safe=False)

@login_required(login_url='login')
def home(request):
    customer = request.user.customer
    customer_medications = customer.medications.all()
    medications_count = customer_medications.count()
    side_effects_list =  customer.my_side_effects_list.all()
    side_effects_count = side_effects_list.distinct().count()
    logs = customer.medlog_set.all()
    symptomlogs_count = customer.symptomlog_set.all().count()
    medlogs_count = logs.count()
    context = {'medications_count': medications_count, 'side_effects_count': side_effects_count,
    'symptomlogs_count': symptomlogs_count, 'medlogs_count': medlogs_count, 'customer_medications': customer_medications, 'logs': logs}
    return render(request, 'users/dashboard.html',context)

@login_required(login_url='login')
def medlogs(request):
    customer = request.user.customer
    logs = customer.medlog_set.all()
    return render(request, 'users/medlogs.html',{'logs':logs})


@login_required(login_url='login')
def symptomlogs(request):
    customer = request.user.customer
    logs = customer.symptomlog_set.all()
    return render(request, 'users/symptomlogs.html',{'logs':logs})

@login_required(login_url='login')
def medications(request):
    customer = request.user.customer
    customer_medications = customer.medications.all()
    return render(request, 'users/medications.html',{'customer_medications':customer_medications})

@login_required(login_url='login')
def data(request):
    return render(request, 'users/data.html')

@login_required(login_url='login')
def friends(request):
    return render(request, 'users/friends.html')
@login_required(login_url='login')
def achievements(request):
    return render(request, 'users/achievements.html')

@login_required(login_url='login')
def medReminders(request):
        return render(request, 'users/medreminders.html')

@login_required(login_url='login')
def addSymptom(request):
    customer = request.user.customer
    form = SideEffectForm(instance=customer)
    return_page = 'symptomlogs'
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = SideEffectForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/symptomlogs')
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/update.html', context)
    return render(request, 'users/addsymptom.html')

@login_required(login_url='login')
def createMedlog(request):
    form = MedlogForm()
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = MedlogForm(request.POST)
        if form.is_valid():
            customer = request.user.customer
            new_medlog = form.save(commit=False)
            new_medlog.customer = customer
            new_medlog.save()
            return redirect('/')
    return_page = 'medlogs'
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/create.html', context)

@login_required(login_url='login')
def updateMedlog(request, pk):
    Medlog = MedLog.objects.get(id=pk)
    form = MedlogForm(instance=Medlog)
    return_page = 'medlogs'
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = MedlogForm(request.POST, instance=Medlog)
        if form.is_valid():
            form.save()
            return redirect('/medlogs')
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/update.html', context)

@login_required(login_url='login')
def deleteMedlog(request,pk):
    Medlog = MedLog.objects.get(id=pk)
    return_page = 'medlogs'
    context = {'return_page': return_page, 'item':Medlog}
    if request.method == 'POST':
        Medlog.delete()
        return render(request, 'users/medlogs.html', context)
    return render(request, 'users/delete.html', context)

@login_required(login_url='login')
def createSymptomLog(request):
    customer = request.user.customer
    form = SymptomLogForm()
    form.fields['side_effect'].queryset = customer.my_side_effects_list.all()
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            customer = request.user.customer
            new_symptomlog = form.save(commit=False)
            new_symptomlog.customer = customer
            new_symptomlog.save()
            return redirect('/symptomlogs')
    return_page = 'symptomlogs'
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/create.html', context)

@login_required(login_url='login')
def updateSymptomlog(request, pk):
    Symlog = SymptomLog.objects.get(id=pk)
    form = SymptomLogForm(instance=Symlog)
    return_page = 'symptomlogs'
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = SymptomLogForm(request.POST, instance=Symlog)
        if form.is_valid():
            form.save()
            return redirect('/symptomlogs')
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/update.html', context)

@login_required(login_url='login')
def deleteSymptomlog(request,pk):
    Symlog = SymptomLog.objects.get(id=pk)
    return_page = 'symptomlogs'
    context = {'return_page': return_page, 'item':Symlog}
    if request.method == 'POST':
        Symlog.delete()
        return render(request, 'users/symptomlogs.html', context)
    return render(request, 'users/delete.html', context)

### Don't create medication, add medication from created list
@login_required(login_url='login')
def createMedication(request):
    form = MedicationForm()
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = MedicationForm(request.POST)
        if form.is_valid():
            customer = request.user.customer
            medication = form.save()
            customer.medications.add(medication)
            side_effects = medication.medication.side_effects.all()
            for se in side_effects  :
                customer.my_side_effects_list.add(se)
            return redirect('/medications')
    return_page = 'medications'
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/create.html', context)

@login_required(login_url='login')
def updateMedication(request, pk):
    medication = Medication.objects.get(id=pk)
    form = MedicationForm(instance=medication)
    return_page = 'medications'
    if request.method == 'POST':
        #print("ATTENTION: ", request.POST)
        form = MedicationForm(request.POST, instance=medication)
        if form.is_valid():
            form.save()
            return redirect('/medications')
    context = {'form': form, 'return_page': return_page}
    return render(request, 'users/update.html', context)

@login_required(login_url='login')
def deleteMedication(request,pk):
    medication = CustomerMedication.objects.get(id=pk)
    return_page = 'medications'
    context = {'return_page': return_page, 'item':medication}
    if request.method == 'POST':
        medication.delete()
        return render(request, 'users/medications.html',context)
    return render(request, 'users/delete.html', context)
