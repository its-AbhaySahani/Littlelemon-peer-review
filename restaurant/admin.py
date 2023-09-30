from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Menu)
admin.site.register(Booking)