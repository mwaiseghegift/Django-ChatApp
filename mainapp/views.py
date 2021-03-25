from django.shortcuts import render

# Create your views here.


def HomePage(request, *args, **kwargs):
    return render(request, 'index.html', {})

def RoomView(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        room_no = request.POST['room-no']
        
        context = {
            'username':username,
            'room_no':room_no,
        }
        
        return render(request, 'room.html', context)
    
    return render(request, 'room.html')