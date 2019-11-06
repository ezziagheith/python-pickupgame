from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addevent/', views.event_create, name="event_create")
]