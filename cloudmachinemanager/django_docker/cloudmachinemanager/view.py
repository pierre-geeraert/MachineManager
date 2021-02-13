import os
import sys

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
sys.path.append("..")
from .test import hello
from .db_interaction import db_interaction


def index(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    output = "Current Time =", current_time
    return HttpResponse(output)

def pwd(request):
    output = hello.say_hello()
    return HttpResponse(output)


def refresh(request):
    template = loader.get_template('hour.html')

    output_db_interaction = db_interaction.main()

    context = {
        'hour_in': output_db_interaction,
    }
    return HttpResponse(template.render(context, request))


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


def cmm(request):
    template = loader.get_template('cmm/index.html')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    output = "Current Time =", current_time

    context = {
        'hour_in': output,
       }
    return HttpResponse(template.render(context, request))

