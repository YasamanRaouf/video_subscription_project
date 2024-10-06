from django import forms
from .models import Video, Subscription, Payment, History


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description'] 



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['user', 'subscription_type', 'start_date', 'end_date', 'price']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'subscription', 'amount', 'payment_date','status']

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ['user', 'video']
