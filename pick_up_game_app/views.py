from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Event, Player, Event_Player
from .forms import EventForm, PlayerForm

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            event_user = Event_User.objects.create(
                user=request.user,
                event=event
            )
            event_user.save()
            return redirect('event_detail', pk=event.pk)       
    else:
        form = EventForm()
    context = {'form':form, 'header': "Add New Event"}
    return render(request, 'event_form.html', context)




def event_edit(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('profile')
    else:
        form=EventForm(instance=event)
    context = {'form': form, 'header': f"Edit {event.name}"}
    return render(request, 'event_form.html', context)


def event_delete(request, pk):
    Event.objects.get(id=pk).delete()
    return redirect('profile')






def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            artist.save()
            return redirect('profile.html', pk=player.pk)
    else:
        form = PlayerForm()
    context = {'form': form, 'header': "Add New Player"}
    return render(request, 'player_form.html', context)

def event_listAll(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, 'events.html', context)

def event(request):
    return HttpResponse("Goodbye rocketshp. Hello Home.")
    

def event_detail(request, pk):
    event_info = Event_User.objects.get(event=pk)
    context = {'event_info': event_info, 'header':'Test Header'}
    return render(request, 'event_info.html', context)


def about(request):
    context = {'about': about, 'header': 'Test Header'}
    return render(request, 'about.html', context)