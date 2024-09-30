# videos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, SubscriptionViewSet, PaymentViewSet, HistoryViewSet, SubscriptionVideoViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'subscription_videos', SubscriptionVideoViewSet)
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Video Subscription Project!")
urlpatterns = [
    path('', include(router.urls)),
    path('', home),
]
