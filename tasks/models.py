from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    
    STATUS_HOLD = 'H'
    STATUS_PROGRESS = 'P' 
    STATUS_DONE = 'D'

    STATUS_CHOISES = [
        (STATUS_HOLD, "On hold"),
        (STATUS_PROGRESS, "In progress"),
        (STATUS_DONE, "Done"),
    ]
    
    status = models.CharField(
        max_length=1, 
        choices=STATUS_CHOISES, 
        default=STATUS_HOLD
    )

    def __str__(self):
        return f'-= {self.title} =-\n\n{self.description}'
