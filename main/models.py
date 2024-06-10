from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files/')
    filename = models.CharField(max_length=100, null=True)
    filetype = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)