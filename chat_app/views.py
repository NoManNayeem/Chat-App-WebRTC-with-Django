from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        'room_name': 'lobby'  # Hardcoded room name for simplicity
    })
