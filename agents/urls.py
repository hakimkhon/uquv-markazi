from django.urls import path
from .views import *

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent_list"),
    path('create/', AgentCreateView.as_view(), name="agent_create")
]
