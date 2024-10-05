from django.db import models
from django.contrib.auth.models import User  # برای استفاده از مدل کاربر

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField()

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # مدل User از django.contrib.auth.models
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    subscription_type = models.CharField(max_length=100)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # مدل User استفاده می‌شود
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # مدل User استفاده می‌شود
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)
