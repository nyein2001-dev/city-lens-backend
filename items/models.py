from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Collaboration(models.Model):
    user = models.ForeignKey(User, related_name='collaborations', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='collaborations', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'project']

    def __str__(self):
        return f"{self.user.username} collaborates on {self.project.name}"

class Ownership(models.Model):
    user = models.ForeignKey(User, related_name='ownerships', on_delete=models.CASCADE)
    project = models.OneToOneField(Project, related_name='ownership', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} owns {self.project.name}"

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
