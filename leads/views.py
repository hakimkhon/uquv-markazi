# from audioop import reverse
from msilib.schema import ListView
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from . import models 
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class HomePage(TemplateView):
    template_name = ("home.html")

class LeadListView(ListView):
    template_name = ("lead\lead_lists.html")
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = ("lead\lead_details.html")
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = ("lead\lead_create.html")
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_lists')

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "forms": form
#     }
#     return render(request, "lead\lead_create.html", context)

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

def lead_delete(request, pk):
    lead = models.Lead.objects.get(id = pk)
    lead.delete()
    return redirect("/leads")
