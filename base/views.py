from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room,Topic
from .form import RoomCreationForm

def home(request):

    q=request.GET.get('q')
    if q:
        rooms=Room.objects.filter(
            Q(topic__name__icontains=q)|
            Q(name__icontains=q)|
            Q(description__icontains=q)|
            Q(host__username__icontains=q)
            )
    else:
        rooms=Room.objects.all()
    rooms_count= rooms.count()
    topics=Topic.objects.all()
    context={'rooms':rooms,'topics':topics,'rooms_count':rooms_count}
    
    return render(request,'base/home.html',context)

def room(request,pk):
    if pk :
        room=Room.objects.get(id=pk)
        context={'room':room}
    else:
        context={}
    return render(request,'base/room.html',context)

def createRoom(request):
    if request.method =='POST':
        form=RoomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Data invalid')
    else:
        form=RoomCreationForm()

    context={'form':form}

    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        form=RoomCreationForm(instance=room,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Invalid Data')
    form=RoomCreationForm(instance=room)
    context={'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    room.delete()
    return redirect('home')