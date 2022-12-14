from django.contrib import admin

# Register your models here.
from .models import User, Airport, Flight, Passenger

admin.site.register(User)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
