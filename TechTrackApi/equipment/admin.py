from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Equipment, Data, Alerts

admin.site.register(Equipment)
admin.site.register(Data)
admin.site.register(Alerts)
