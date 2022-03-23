from pyexpat import model
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
            return redirect("/leads")
    context = {
        "forms": form
    }
    return render(request, "lead\lead_create.html", context)

def lead_update(request, pk):
    lead = models.Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form, "lead": lead
    }
    return render(request, "lead\lead_update.html", context)
