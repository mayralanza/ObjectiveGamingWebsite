from OBJusers.models import Event, Team
from rest_framework import serializers
from django.contrib.auth.models import User

        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Event
        fields = ['event', 'description','team', 'created_at']
