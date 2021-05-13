from django.shortcuts import render

from .models import information
# Create your views here.


def contactus(request):
    informationdata = information.objects.all()[0]

    context = {
    'contactlist': informationdata,
    }

    return render(request, "contact.html", context)
