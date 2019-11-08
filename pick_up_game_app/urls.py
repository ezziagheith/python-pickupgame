from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addevent/', views.event_create, name="event_create"),
    path('addplayer/', views.player_create, name="player_create"),
    path('events/<int:pk>', views.event_detail, name="event_detail"),
    path('events/edit_event/<int:pk>', views.event_edit, name='event_edit'),
    path('events/<int:pk>/delete/', views.event_delete, name= 'event_delete')
    # path('about/', views.aboutus, name ='about'),
    

]