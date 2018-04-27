from django.contrib import admin

# Register your models here.
from . models import Person, Manufacturer, Car, Publication


class PersonAdmin(admin.ModelAdmin):

	list_display = ['name','shirt_size','add_date']



admin.site.register(Person, PersonAdmin)
admin.site.register(Manufacturer)

