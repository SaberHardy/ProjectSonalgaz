# from django.db import models
# import uuid
#
#
# class File(models.Model):
#     title = models.CharField(max_length=100)
#     file = models.FileField(upload_to='files/')
#     # uploader = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="files")
#     # created_at = models.DateTimeField
#     updated_at = models.DateTimeField(auto_now=True)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     def __str__(self):
#         return self.title
