import os

from django.db import models
import uuid


class File(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return os.path.basename(self.file.name)

    def filename(self):
        return os.path.basename(self.file.name)
