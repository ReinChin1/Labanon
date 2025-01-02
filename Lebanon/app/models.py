from django.db import models

class BlotterEntry(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    date = models.DateField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
