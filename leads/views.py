# from audioop import reverse
from msilib.schema import ListView
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from . import models 
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class HomePage(TemplateView):
    template_name = ("home.html")

class SignupView(CreateView):
    template_name = ("registration/signup.html")
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadListView(ListView):
    template_name = ("lead/lead_lists.html")
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = ("lead/lead_details.html")
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = ("lead/lead_create.html")
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadUpdateView(UpdateView):
    template_name = ("lead\lead_update.html")
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_lists')

class LeadDeleteView(DeleteView):
    template_name = ("lead\lead_delete.html")
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_lists')
