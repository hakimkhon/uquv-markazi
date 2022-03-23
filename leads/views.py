from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from . import models 
from .forms import *

def home(request):
    return render(request, "home.html")

def lead_lists(request):
    lead = models.Lead.objects.all
    context = {
        "leads": lead
    }
    return render(request, "lead\lead_lists.html", context)

def lead_details(request, pk):
    lead = get_object_or_404(models.Lead, id = pk)
    context = {
        "lead": lead
    }
    return render(request, "lead\lead_details.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # ism = form.cleaned_data['ism']
            # famila = form.cleaned_data['famila']
            # yosh = form.cleaned_data['yosh']
            # agent = models.Agent.objects.first()
            # models.Lead.objects.create(
            #     ism = ism, 
            #     famila = famila, 
            #     yosh = yosh,
            #     agent = agent,
            # )
            return redirect("/leads")
    context = {
        "forms": form
    }
    return render(request, "lead\lead_create.html", context)



# def student_create(request):
#     print(request.POST)
#     form = StudentForm()
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             print("Malumotlar")
#             print(form.cleaned_data)
#             ism = form.cleaned_data['ism']
#             famila = form.cleaned_data['famila']
#             yosh = form.cleaned_data['yosh']
#             teacher = models.Teacher.objects.first()
#             models.Student.objects.create(
#                 ism = ism, famila = famila, yosh = yosh,teacher = teacher,
#             )
#             print("Muvofiqiyat")
#     context = { forms": form }
#     return render(request, "student_create.html", context)

