from django.db import models
import os

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files/')
    filetype = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.file.name)