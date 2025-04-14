from django.urls import path

from .views import (TaskListView, TagListView, TagDeleteView,
                    TagUpdateView, TagCreateView, change_task_status,
                    TaskCreateView, TaskUpdateView, TaskDeleteView)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change_status", change_task_status, name="task-change-status"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
]
