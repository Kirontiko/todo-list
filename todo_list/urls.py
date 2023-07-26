from django.urls import path

from todo_list.views import (IndexView,
                             TagListView,
                             TaskCreateView,
                             TagCreateView,
                             TaskUpdateView,
                             TaskDeleteView, TagDeleteView, TagUpdateView, UserCreateView, TaskUpdateCompleteStateView,
                             TagDetailView)


urlpatterns = [
    path("",
         IndexView.as_view(),
         name="index"),
    path("tags/",
         TagListView.as_view(),
         name="tag-list"),
    path("tags/<int:pk>/",
         TagDetailView.as_view(),
         name="tag-detail"),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"),
    path("tags/<int:pk>/update",
         TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete",
         TagDeleteView.as_view(),
         name="tag-delete"),
    path("task_create/",
         TaskCreateView.as_view(),
         name="task-create"),
    path("<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
    path("<int:pk>/update_state/",
         TaskUpdateCompleteStateView.as_view(),
         name="task-update-state"),
    path("user_create/",
         UserCreateView.as_view(),
         name="user-create"),
]

app_name = "todo_list"
