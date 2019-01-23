from django.db import models

# Create your models here.
class Todo(models.Model):
    tasks = models.CharField(max_length=120)
    task_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.tasks
