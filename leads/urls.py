from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', lead_lists, name="lead_lists"),
    path('<int:pk>/', lead_details, name="lead_details"),
    path('<int:pk>/uzgartirish/', lead_update, name="lead_update"),
    path('<int:pk>/uchirish/', lead_delete, name="lead_delete"),
    path('yaratish/', lead_create, name="lead_create"),
]
