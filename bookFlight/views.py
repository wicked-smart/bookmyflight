from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Airport, Passenger, Flight
# Create your views here.

def index(request):
    try:
        flights = Flight.objects.all()
        return render(request, 'bookFlight/index.html', {'flights': flights})

    except Flight.DoesNotExist:
        return render(request, 'bookFlight/index.html', {'message': 'Flight Database Does Not Exsist!'} )

   


def flight(request, id):
    try:
        flight = Flight.objects.get(pk=id)
        passengers= flight.passengers.all()
        non_passengers = Passenger.objects.exclude(flight=flight)
        print(passengers)


        return render(request, 'bookFlight/flight.html', 
        {
            'flight': flight,
            'passengers': passengers,
            'non_passengers': non_passengers
        })
    
    except Flight.DoesNotExist:
        return render(request, 'bookFlight/index.html', {'message': 'Flight Database Does Not Exsist!'} )
