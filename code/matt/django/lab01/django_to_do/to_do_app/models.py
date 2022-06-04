# from turtle import settiltangle
from django.db import models
import datetime as dt

priority_level = [("high", "high"), ("medium", "medium"), ("low", "low")]


class Priorities(models.Model):
    setting = models.CharField(max_length=6, choices=priority_level)

    def __str__(self) -> str:
        return self.setting


class TodoItem(models.Model):

    text = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    task_complete = models.BooleanField(default=False)
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
