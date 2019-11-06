from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Event
from .forms import EventForm

# Create your views here.
def home(request):
    return HttpResponse('Updating home page')


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    context = {'form':form, 'header': "Add New Event"}
    return render(request, 'event_form.html', context)