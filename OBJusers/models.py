from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class Team(models.Model):
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')  
    bio = models.TextField(default='', null=True)
    role = models.CharField(max_length=200) 
    game_id = models.TextField(default='')

    def __str__(self):
        return self.team.team_name + ": " + self.member.username

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    event = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.TextField()
    #event_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ManyToManyField (User, related_name='events')

    def __str__(self):
        return self.event + "\n" + self.description

class Profile(models.Model):
    user = models.ManyToManyField (User)
    followsEvent = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.followsEvent.event



