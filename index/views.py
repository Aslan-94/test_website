from django.shortcuts import render
from django.http import HttpResponse

from .models import about, slider, client # necessary to import in order to present on front-end
# Create your views here.

def home(request): # 0 is index of about in backend / or add it in index.html
    aboutdata = about.objects.all()[0] # takes all data from models.py /  def __str__(self): - is an object
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    context = {
        'about': aboutdata,
        'slider': sliderdata,
        'client': clientdata
    }

    return render(request, 'index.html', context)

def aboutus(request):  # method and module names should not be the same
    return render(request, 'about.html')
