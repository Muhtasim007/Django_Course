from django.urls import path
from . import views

urlpatterns = [
    path('overdue-tasks/', views.overdue_tasks_view, name='overdue_tasks'),
]
