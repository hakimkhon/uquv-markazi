from urllib.parse import urlparse
from django.urls import URLPattern, path
from .views import *

name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent_lists")    
]