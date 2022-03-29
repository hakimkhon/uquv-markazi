from leads.models import Agent
from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agents_list.html"
    
    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')       

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofil
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse("agents:agent_list")

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/agents_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse("agents:agent_list")
    