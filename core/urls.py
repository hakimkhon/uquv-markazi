
from django.contrib import admin
from django.urls import path, include
from leads.views import HomePage
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('leads/', include('leads.urls', namespace = "leads")),
    path('login/', LoginView.as_view(), name = "login"),
]
