from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import os
#from .models import Question
from datetime import datetime


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    output = "Current Time =", current_time
    return HttpResponse(output)

def pwd(request):
    output = os.system("pwd")
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