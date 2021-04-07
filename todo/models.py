from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4


User = get_user_model()


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    subject = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)


class TodoComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(blank=True, default="")


class TodoCommentAttachment(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d')
    comment = models.ForeignKey(
        TodoComment, on_delete=models.CASCADE, related_name="files")
