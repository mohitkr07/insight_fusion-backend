from django.db import models

# Create your models here.
class Conversation(models.Model):
    scenario = models.TextField()
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
