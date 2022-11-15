from django.db import models
from user import User
from tag import Tag


class Task(models.Model):
    class States(models.TextChoices):
        NEW = "new_task"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=60)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL)
    expired_at = models.DateField()
    priority = models.IntegerField()
    state = models.CharField(max_length=20, default=States.NEW, choices=States.choices)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL)
