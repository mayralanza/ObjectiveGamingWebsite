from django.contrib import admin
from .models import Team, Event, Profile, TeamMember

# Register your models here.
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(TeamMember)