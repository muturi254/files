from ipaddress import ip_address
from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=25, blank=True)
    document = models.FileField(upload_to='data/')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description


class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    gender = models.CharField(max_length=9)
    ip_address = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "{0} - {1}".format(self.first_name, self.last_name)