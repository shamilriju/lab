from django.contrib import admin
from lab.models import *
# Register your models here.
class tester(admin.ModelAdmin):
    list_display =['test_name','description','rate','procedures']
    list_editable =['description','rate','procedures']
admin.site.register(test,tester)

class books(admin.ModelAdmin):
    list_display = ['name','email','phone','age','date','test','message']
admin.site.register(bookings,books)
