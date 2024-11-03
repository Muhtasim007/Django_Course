from django.shortcuts import render
from django.utils import timezone
from .models import Task

def overdue_tasks_view(request):
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now())
    return render(request, 'tasks/overdue_tasks.html', {'overdue_tasks': overdue_tasks})
