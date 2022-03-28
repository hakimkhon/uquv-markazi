from django.urls import path
from .views import *

app_name = "agents"

urlpatterns = [
    path('', AgentHomePage.as_view(), name="agent_list")
]
