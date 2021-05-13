from django.db import models

# Create your models here.

class information(models.Model):
    address = models.TextField(max_length = 800, blank = False)
    email = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.email
