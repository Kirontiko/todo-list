from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateOrUpdateForm
from todo_list.models import Task, Tag


class IndexView(generic.View):
    model = Task

    def get(self, request):
        context = {
            "task_list": Task.objects.all().prefetch_related(
                "tags"
            ).select_related("user")
        }

        return render(request,
                      "todo_list/index.html",
                      context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateOrUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateOrUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


