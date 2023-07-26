from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractUser):
    pass


class Task(models.Model):
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="tasks",
                             on_delete=models.CASCADE)
