from django.db import models

# Create your models here.

class Content(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.TextField(max_length=400)

    def __str__(self):
        return self.name