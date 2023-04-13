from django.urls import path 
from .views import EventViewSet, UserCreate

urlpatterns = [
    path('', EventViewSet.as_view({'get': 'list'}) ),
    path('post', UserCreate.as_view() ),
]