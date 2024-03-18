from django.shortcuts import render
from django.http import HttpResponse

def mechanical(request, equipment=None):
    if equipment is None:
        return HttpResponse("No equipment specified. Use http://localhost:8000/mechanical/equipmentValue")
    else:
        return HttpResponse(f"Equipment: {equipment}")
    
def render_mechanical_template(request):
    return render(request, 'mechanical.html')