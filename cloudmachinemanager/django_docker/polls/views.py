import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
#from cloudmachinemanager.db_interaction import testingg


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    output = "Current Time =", current_time
    return HttpResponse(output)

def pwd(request):
    output = "testingg"
    return HttpResponse(output)




def template(request):
    template = loader.get_template('hour.html')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    output = "Current Time =", current_time

    context = {
        'hour_in': output,
       }
    return HttpResponse(template.render(context, request))
    #return render(request, 'hour.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
