from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"{self.content}"
