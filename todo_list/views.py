from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateOrUpdateForm, UserCreateForm
from todo_list.models import Task, Tag, User


class IndexView(generic.ListView):
    model = Task
    paginate_by = 3
    template_name = "todo_list/index.html"
    def get_queryset(self):
        self.queryset = Task.objects.filter(user__id=self.request.user.id)

        return self.queryset


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateOrUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskCreateOrUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("login")


class TaskUpdateCompleteStateView(LoginRequiredMixin, generic.UpdateView):
    def post(self, request, *args, **kwargs) -> redirect:
        task = get_object_or_404(Task, pk=kwargs["pk"])

        task.is_completed = not task.is_completed
        task.save()

        return redirect("todo_list:index")



