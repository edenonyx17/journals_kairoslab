from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class journal(models.Model):
    topic = models.CharField(max_length=100)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

