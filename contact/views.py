from django.shortcuts import render

from .models import information
from .models import contactform
# Create your views here.


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # first name is the name of contactform and second from request methos == "POST"
        contactformdata = contactform(name = name, email = email, subject = subject, message = message)
        contactformdata.save()


    informationdata = information.objects.all()[0]

    context = {
    'contactlist': informationdata,
    }

    return render(request, "contact.html", context)
