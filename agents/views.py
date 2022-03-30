from leads.models import Agent
from django.urls import reverse
# from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .mixins import OrganiserAndLoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(OrganiserAndLoginRequiredMixin, ListView):
    template_name = "agents/agents_list.html"
    
    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

class AgentCreateView(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')       

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofil
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

class AgentUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse("agents:agent_list")

class AgentDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = "agents/agents_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofil
        return Agent.objects.filter(organisation = organisation)

    def get_success_url(self):
        return reverse("agents:agent_list")
    