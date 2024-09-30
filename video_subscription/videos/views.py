# videos/views.py
from rest_framework import viewsets
from .models import Video, Subscription, Payment, History, SubscriptionVideo
from .serializers import VideoSerializer, SubscriptionSerializer, PaymentSerializer, HistorySerializer, SubscriptionVideoSerializer

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

class SubscriptionVideoViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionVideo.objects.all()
    serializer_class = SubscriptionVideoSerializer
