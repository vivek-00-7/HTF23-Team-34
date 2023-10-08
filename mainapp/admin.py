from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Equip)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('eq_id','name','quantity_available')

@admin.register(Book)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','equipment','booking_time','branch','section','status')