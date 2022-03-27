
from django.contrib import admin
from django.urls import path, include
from leads.views import HomePage, SignupView
from django.contrib.auth.views import LoginView, LogoutView
from agetns.views import AgentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('leads/', include('leads.urls', namespace = "leads")),
    path('login/', LoginView.as_view(), name = "login"),
    path('signup/', SignupView.as_view(), name = "signup"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('agents/', include('agents.urls', namespace = "agents")),
]
