from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VideoViewSet,
    SubscriptionViewSet,
    PaymentViewSet,
    HistoryViewSet,
    home_view,
    profile_view,
    video_list_view,
    subscription_view,
    create_video_view,
    create_subscription_view,
    create_payment_view,
    create_watch_history_view,
)

router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'histories', HistoryViewSet)

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),  # API URLs

    # Template routes
    path('', home_view, name='home'),  # صفحه اصلی
    path('profile/', profile_view, name='profile'),  # صفحه پروفایل
    path('videos/', video_list_view, name='video_list'),  # لیست ویدیوها
    path('subscription/', subscription_view, name='subscription'),  # صفحه اشتراک‌ها
    path('videos/create/', create_video_view, name='create_video'),  # ایجاد ویدیو
    path('subscriptions/create/', create_subscription_view, name='create_subscription'),  # ایجاد اشتراک
    path('payments/create/', create_payment_view, name='create_payment'),  # ایجاد پرداخت
    path('watch-history/create/', create_watch_history_view, name='create_watch_history'),  # ایجاد تاریخچه تماشا
]
