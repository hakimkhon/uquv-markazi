from audioop import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, ListView):
    template_name = ("agent/agent_list.html")
    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = ("agent/agent_create.html")
    form_class = AgentModelForm
    def get_success_url(self):
        return reverse('agents:agent_list')       

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profil = self.request.user.userprofil
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agent/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.all()

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agent/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent_list")

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agent/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self, get_response):
        return reverse('agents:agent_list')
    