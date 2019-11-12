from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Event, Player, Event_Player, Event_User
from .forms import EventForm, PlayerForm

from django.utils.text import slugify

# Create your views here.
def landing(request):
    return render(request,'landing.html')

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.slug_string = f"{event.name}-{event.date}-{event.location}"
            event.slug = slugify(event.slug_string)
            event.save()
            event_user = Event_User.objects.create(
                user=request.user,
                event=event
            )
            event_user.save()
            return redirect('event_detail', event_slug=event.slug)       
    else:
        form = EventForm()
    context = {'form':form, 'header': "Add New Event"}
    return render(request, 'event_form.html', context)

# def event_detail(request, pk):
#     event_detail = Event_User.objects.get(event=pk)
#     context = {'event_detail': event_detail, 'header':'Test Header'}
#     return render(request, 'event_detail.html', context)

@login_required
def event_detail(request, event_slug):
    event_detail = Event.objects.get(slug=event_slug)
    context = {'event_detail': event_detail, 'header': f"{event_detail.name} Details"}
    return render(request, 'event_detail.html', context)

@login_required
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

@login_required
def event_delete(request, pk):
    Event.objects.get(id=pk).delete()
    return redirect('profile')

@login_required
def event_join(request, pk):
    event = Event.objects.get(id=pk)
    event_user = Event_User.objects.create(
        user=request.user, 
        event=event
    )
    event_user.save()
    return redirect('profile')

@login_required
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.save()
            return redirect('profile')
    else:
        form = PlayerForm()
    context = {'form': form, 'header': "Add New Player"}
    return render(request, 'player_form.html', context)

# def player_edit(request, pk):
#     player = Player.objects.get(id=pk)
#     if request.method == 'POST':
#         form = PlayerForm(request.post, instance=player)
#         if form.is_valid():
#             player = form.save()
#             return redirect('profile')
#     else:
#         form = PlayerForm(instance=player)
#     context = {'form': form, 'header': f"Edit {player.user.username} Profile", 'player': 'player'}
#     return render(request, 'player_form.html', context)



def event_listAll(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, 'events.html', context)


def about(request):
    context = {"about": about}
    return render(request, 'about.html', context)

