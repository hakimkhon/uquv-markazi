from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = ("agent/agent_list.html")

    def get_queryset(self):
        return Agent.objects.all() 