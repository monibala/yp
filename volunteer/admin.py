from django.contrib import admin

from .models import become_volunteer, volunteer_info

# Register your models here.
admin.site.register(volunteer_info)
admin.site.register(become_volunteer)