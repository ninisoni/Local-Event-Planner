from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

def index(request):
    events = Event.objects.all()
    return render(request, 'files/index.html', {'events': events})

def event_detail(request, title):
    event = get_object_or_404(Event, title=title)
    return render(request, 'files/event_detail.html', {'event': event})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'files/add_event.html', {'form': form})
