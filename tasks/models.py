from tkinter import CASCADE
from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField("", auto_now=False)
    due_date = models.DateTimeField("", auto_now=False)
    is_complete = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        "auth.User",
        null=True,
        related_name="tasks",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

