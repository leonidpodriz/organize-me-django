from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    subject = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
