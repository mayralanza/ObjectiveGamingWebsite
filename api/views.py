from OBJusers.models import Event
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import EventSerializer, UserSerializer
from django.contrib.auth.models import User

class EventViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.save()
            new_user = UserSerializer(user)
            return Response(new_user.data)
        else:
            return Response(serializer.errors)