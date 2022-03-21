from django.shortcuts import render
from django.http import HttpResponse
from . import models 

def home(request):
    return render(request, "home.html")

def lead_lists(request):
    lead = models.Lead.objects.all
    context = {
        "leads": lead
    }
    return render(request, "lead\lead_lists.html", context)

# def lead_details(request, pk):
#     print(pk)
#     lead = models.Lead.objects.get(id = pk)
#     print(lead)
#     return render(request, "lead_details.html")

