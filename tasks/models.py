from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completion_status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self) -> str:
        return (f"Task: {self.content[:50]}{'...' if len(self.content) > 50 else ''}"
                f" (Done: {self.completion_status})")

    class Meta:
        ordering = ['completion_status', '-created_at']

