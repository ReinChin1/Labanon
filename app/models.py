from django.db import models
from django.contrib.auth.models import User

class BlotterEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

