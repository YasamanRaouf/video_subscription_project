# videos/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Video, Subscription, Payment, History
from .serializers import VideoSerializer, SubscriptionSerializer, PaymentSerializer, HistorySerializer

# API ViewSets
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

# Template Views
def home_view(request):
    return render(request, 'home.html')

def profile_view(request):
    # Assuming we have a 'Subscription' relationship with the User
    return render(request, 'profile.html', {'user': request.user})

def video_list_view(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def subscription_view(request):
    subscription = request.user.subscription  # Assuming there's a OneToOne relationship between User and Subscription
    return render(request, 'subscription.html', {'subscription': subscription})
