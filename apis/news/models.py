from django.db import models
from apis.accounts.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    story = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
