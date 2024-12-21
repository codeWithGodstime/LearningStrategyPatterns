from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)