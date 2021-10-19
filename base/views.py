from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room
from .form import RoomCreationForm

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    
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