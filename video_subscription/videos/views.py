from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Video, Subscription, Payment, History
from .serializers import VideoSerializer, SubscriptionSerializer, PaymentSerializer, HistorySerializer
from .forms import VideoForm, SubscriptionForm, PaymentForm, HistoryForm

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

# New Views for Forms
def create_video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'create_video.html', {'form': form})

def create_subscription_view(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'create_subscription.html', {'form': form})

def create_payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form})

def create_watch_history_view(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('watch_history_list')
    else:
        form = HistoryForm()
    return render(request, 'create_watch_history.html', {'form': form})
