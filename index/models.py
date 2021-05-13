from django.db import models

# Create your models here.

class about(models.Model):
    title = models.CharField(max_length = 100, blank = False) # if False we can't keep this field blank
    description = models.TextField(max_length = 800, blank = False)
    image = models.ImageField(upload_to = 'about/', blank = False)

    def __str__(self):
        return self.title

# 1 makemigration
# 2 migrate
# register in index admin.py

class slider(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    description = models.TextField(max_length = 800, blank = True)
    image = models.ImageField(upload_to = 'slider/', blank = True)

    def __str__(self):
        return self.title


class client(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    link = models.CharField(max_length = 100, blank = True)
    image = models.ImageField(upload_to = 'client/', blank = True)

    def __str__(self):
        return self.name
