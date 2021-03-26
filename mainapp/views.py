from django.shortcuts import render
from .models import Chat
# Create your views here.


def HomePage(request, *args, **kwargs):
    return render(request, 'index.html', {})

def RoomView(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        room_no = request.POST['room-no']
        messages = []
        
        chat = Chat.objects.filter(room_no = room_no)
        for obj in chat:
            messages.append(obj.message)
        context = {
            'username':username,
            'room_no':room_no,
            'messages':messages,
        }
        
        return render(request, 'room.html', context)
    
    return render(request, 'room.html')