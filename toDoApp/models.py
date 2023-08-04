from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=6000 , null=True , blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.author}'