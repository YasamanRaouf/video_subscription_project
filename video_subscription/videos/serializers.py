# videos/serializers.py
from rest_framework import serializers
from .models import Video, Subscription, Payment, History, SubscriptionVideo

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class SubscriptionVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionVideo
        fields = '__all__'
