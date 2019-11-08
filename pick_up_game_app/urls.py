from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addevent/', views.event_create, name="event_create"),
    path('addplayer/', views.player_create, name="player_create"),
    path('events/', views.event, name="event"),
    path('events/event_test/<int:pk>', views.event_test, name="event_test")
    # path('events/<int:pk>', views.event_detail, name="event_detail"),
]