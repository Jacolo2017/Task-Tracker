from django.shortcuts import render
from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    related_name = "projectlist"

    def qet_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"
    related_name = "projectdetail"
