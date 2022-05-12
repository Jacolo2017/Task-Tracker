from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from tasks.models import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])


class TaskListView(ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["is_complete"]

    def get_success_url(self):
        return reverse_lazy("show_my_tasks", args=[self.object.id])
