from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent

class AgentHomePage(LoginRequiredMixin, ListView):
    template_name = ("agent/agent_list.html")
    def get_queryset(self):
        return Agent.objects.all()
