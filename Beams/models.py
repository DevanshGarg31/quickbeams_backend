from django.db import models

# Create your models here.
class Beam(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    walkthrough_video = models.URLField(blank=True, null=True)  # URL of the walkthrough video
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    
    def __str__(self):
        return self.name