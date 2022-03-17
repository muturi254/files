from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=25, blank=True)
    document = models.FileField(upload_to='data/')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description