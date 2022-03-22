from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', home),
    path('leads/', lead_lists),
    path('leads/<int:pk>/', lead_details),
    path('leads/create/', lead_create),
]
