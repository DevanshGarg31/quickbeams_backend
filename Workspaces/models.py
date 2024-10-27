from django.db import models
from Accounts.models import *


# Create your models here.

# Company Model
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    admin = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name

# Workspace Model
class Workspace(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='workspaces')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# UserWorkspace Model
class UserWorkspace(models.Model):
    USER_TYPES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='user_workspaces')
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='user_workspaces')
    type = models.CharField(max_length=10, choices=USER_TYPES)

    class Meta:
        unique_together = ('user', 'workspace')

    def __str__(self):
        return f"{self.user.username} - {self.workspace.name}"
