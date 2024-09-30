from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    subscription_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.amount} for {self.user.username}"

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} watched {self.video.title}"

class SubscriptionVideo(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscription} - {self.video.title}"
