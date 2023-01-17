import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import datetime, timedelta


def index(request):
    d = Doctor.objects.all()
    return render(request, "Doc_Appoint/index.html", {'d': d})
    # return HttpResponse("Hello, world!")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Doc_Appoint/login.html", {
                "message": "Invalid username and/or password. Try Again!!"
            })
    else:
        return render(request, "Doc_Appoint/login.html", {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request, user_selection):
    if user_selection == 'personal' or user_selection == "doctor":
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmation = request.POST['confirmation']
            user_type = user_selection
            if password != confirmation:
                return render(request, "Doc_Appoint/register.html", {
                    "message": "Passwords entered do not match"
                })
            try:
                user = User.objects.create_user(username, email, password)
                if user_selection == 'doctor':
                    user.user_type = 'DR'
                else:
                    user.user_type = 'PR'
                user.save()
            except IntegrityError:
                return render(request, "Doc_Appoint/register.html", {
                    "message": "Username already taken"
                })
            if user_selection == 'doctor':
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('next'))
            else:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "Doc_Appoint/register.html", {})
    else:
        return HttpResponse("error")

def select(request):
    return render(request, "Doc_Appoint/selection.html")

def next_steps(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'DR':
            if request.method == 'POST':
                doc_user = User.objects.get(id=request.user.id)
                services = request.POST['services']
                experience = request.POST['experience']
                study = request.POST.get('study')
                phone = request.POST.get('phone_number')
                service_time_from = request.POST.get('service_time_from')
                service_time_to = request.POST.get('service_time_to')
                address = request.POST.get('address')
                try:
                    new_doctor = Doctor.objects.create(doctor_name=doc_user,
                        services=services,
                        experience=experience,
                        study=study,
                        phone_number=phone,
                        service_time_from=service_time_from,
                        service_time_to=service_time_to,
                        address=address
                    )
                    new_doctor.save()
                except IntegrityError:
                    return render(request, "Doc_Appoint/next_steps_doc.html", {
                        "message": "Something went wrong"
                    })
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "Doc_Appoint/next_steps_doc.html")
        else:
            return HttpResponse('Error, user is not a doctor!')
    else:
        return HttpResponse('User not logged in!')

# Dashboard
def dashboard_doc(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'DR':
            return render(request, "Doc_Appoint/dashboard_doc.html", {})
        else:
            return HttpResponse('This is not a doctor\'s account')
    else:
        return HttpResponse("User not logged in!")


def dashboard_personal(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'PR':
            if request.method == 'POST':
                if 'search' in request.POST:
                    query = request.POST.get('q')
                    doc_name, err = search_doctors(query)
                    return render(request, "Doc_Appoint/dashboard_personal.html", {
                        'doc_name': doc_name,
                        'err': err
                    })
                # if 'booking' in request.POST:
                #     # return HttpResponse('booking')
                #     return HttpResponseRedirect('book-appointment')
            else:
                return render(request, "Doc_Appoint/dashboard_personal.html", {
                })
        else:
            return HttpResponse('This is not a personal account')
    else:
        return HttpResponse("User not logged in!")

def search_patients(request, query):
    pass

def search_doctors(query):
    doc = Doctor.objects.all()
    results = []
    found = False
    error = False
    if len(query) != 0:
        # searching by name & services
        for name in doc:
            if query.lower() in name.doctor_name.username.lower() or query.lower() in name.services.lower():
                if query.lower() == name.doctor_name.username.lower():
                    u_id = User.objects.get(username=query)
                    doc_name_get = Doctor.objects.get(doctor_name = u_id)
                    results.append(doc_name_get)
                    # return results, error
                else:
                    # sub_query_name.append(name.doctor_name.username)
                    u_id_sub = User.objects.get(username=name.doctor_name.username)
                    doc_name_get_sub = Doctor.objects.get(doctor_name = u_id_sub)
                    results.append(doc_name_get_sub)
                    # return results, error
                # if query.lower() == name.services.lower():
                #     doc_service = Doctor.objects.filter(services=name.services)
                #     results.append(doc_service)
                    # return results, error
                # else:
                #     results.append(name)
                    # return results, error
                found = True
        if not found:
            error = True
        return results, error
    else:
        error = True
        return results, error


def time_slots(doc_id):
    slots = {}   
    doc = Doctor.objects.get(id=doc_id)
    t1 = doc.service_time_from.strftime("%H:%M:%S")
    t2 = doc.service_time_to.strftime("%H:%M:%S")
    time_from = datetime.strptime(t1, "%H:%M:%S")
    time_to = datetime.strptime(t2, "%H:%M:%S")
    diff = time_to - time_from
    diff_min = diff.seconds / 60
    diff_hour = diff_min / 60 
    ts = time_from

    ''' 
        creating time slots based on 30 minutes diff
        that is why multiplying by 2 so, we have 2 slots every hour.
        storing those slots in a dict, and every slot has a value of False in the beginning.
        if it gets filled, we'll set it to true.
    '''
    for i in range(int(diff_hour)*2):
        ts = ts + timedelta(minutes=30)
        slots[ts.time()] = False

    return slots
    
@login_required
def book_appointment(request, doc_id):
    doc = Doctor.objects.get(id = doc_id)
    booking_times = time_slots(doc_id)
    return render(request, "Doc_Appoint/book_appointment.html", {
        'doc': doc,
        'booking_times': booking_times
    })
























    # search
    # for n in doc_names:
    #     if query.lower() in n.lower():
    #         if query.lower() == n.lower():
    #             doc_name_filter = Doctor.objects.filter(doc.doctor_name.username)
    #             found_name = True
    #         else:
    #             sub_query_name.append(n)
    #         found_name = True
    # if not found_name:
    #     error_name = True
    #     found_name = False
        
    # for s in doc_services:
    #     if query.lower() in s.lower():
    #         if query.lower() == s.lower():
    #             return HttpResponse('found', query)
    #         else:
    #             sub_query_service.append(s)
    #         found_service = True
    # if not found_service:
    #     error_service = True

    # return found_name, query

# def search(request):
#     # searches for the enteries based on the string entered in the search box. Returns a list of the matched enteries if a substring is entered.
#     # If a string is entered and it fully matches the value in the enteries folder, it redirects to the entry page for that entry.
#     query = request.GET.get("q")
#     sub=[]
#     # Setting the flags to false so if a certain condition is met, they are set to true.
#     error=False
#     found=False
#     for st in util.list_entries():   
#         if query.lower() in st.lower():
#             if query.lower() == st.lower():
#                 return redirect("entryPage", title=query)
#             else:
#                 sub.append(st) # add to the sub list when an entry is found based on the search(a sub string and not a whole string)
#             found = True   
#     if not found:
#         error = "True"
#     return render(request, "encyclopedia/search.html",{
#         "query": query,
#         "sub": sub,
#         "error": error
#     })