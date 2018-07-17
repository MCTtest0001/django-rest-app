from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=140, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
