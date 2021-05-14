from django.contrib import admin

from .models import information
from .models import contactform

# Register your models here.

admin.site.register(information)
admin.site.register(contactform)