from audioop import reverse
from django.views.generic import ListView, CreateView
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
        return reverse('leads:lead_lists')        
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profil = self.request.user.userprofil
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

