from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        return self.due_date < timezone.now()
