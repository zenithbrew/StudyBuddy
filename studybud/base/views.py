from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm


# rooms = [
#     {"id": 1, "name": "Lets learn python!"},
#     {"id": 2, "name": "Lets learn "},
#     {"id": 3, "name": "Lets python!"},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |        
        Q(description__icontains=q) |
        Q(host__username__icontains=q)) 
    # 'topic' is column name then '__' takes to parent then 'name' is column name, __icontains for string matching
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=int(pk))
    context = {'room': room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)

def update_room(request, pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)

def delete_room(request, pk):
    room = Room.objects.get(id=int(pk))
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})