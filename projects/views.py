from django.shortcuts import render
from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    related_name = "projects_list"

    def qet_queryset(self):
        return Project.objects.filter(members=self.request.user)
