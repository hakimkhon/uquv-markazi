from django.shortcuts import render
from django.http import HttpResponse
from . import models 

def home(request):
    lead = models.Lead.objects.all
    context = {
        "leads": lead
    }
    return render(request, "home.html", context)

def lead_details(request, pk):
    print(pk)
    lead = models.Lead.objects.get(id = pk)
    print(lead)
    return render(request, "lead_details.html")

