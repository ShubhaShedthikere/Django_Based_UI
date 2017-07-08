# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import NameForm,StartForm,EndForm,MobileNoForm
import json
from kafka import KafkaProducer


class Producer:

    init_flag = False
    def __init__(self):

        try:

            self.kafkaproducer = KafkaProducer(
                bootstrap_servers=str("localhost:9092"),
                retries=int(3),
                max_request_size=1048576)
            self.topic = "user_info"
        except:
            print "Cannot start kafka producer"
            exit()
        print "Initializing Kafka Producer"

    def send(self, mobile_no, json_string):
        self.kafkaproducer.send(topic=str(self.topic), value=json_string, key=str(mobile_no))
        return

kafka_prod_obj = Producer()

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print "here"
            # redirect to a new URL:
            return HttpResponse("I have done my action")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        template = loader.get_template('traffic_app/name.html')
        context = {'form': form}
    return HttpResponse(template.render(context,request))

def index(request):

    Sform = StartForm()
    Eform = EndForm()
    template = loader.get_template('index.html')
    context = {'Sform': Sform,'Eform':Eform}
    return HttpResponse(template.render(context, request))
    #return HttpResponse("I have done my action")

def user_form(request):

    Sform = StartForm()
    Eform = EndForm()
    Mform = MobileNoForm()
    template = loader.get_template('user_form.html')
    context = {'Sform': Sform, 'Eform': Eform,"Mform":Mform}

    if request.method == "POST":
        print request.POST
        starting_point = request.POST["starting_point"]
        ending_point = request.POST["ending_point"]
        mobile_no = request.POST["mobile_no"]
        print "it is a post %s" % starting_point
        print "destination %s" % ending_point
        print "mobile_no %s" % mobile_no



    return HttpResponse(template.render(context, request))

def performance(request):

    template = loader.get_template('performance.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):

    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def callbacks(request):

    if request.method == "POST":
        print request.POST
        starting_point = request.POST["starting_point"]
        ending_point = request.POST["ending_point"]
        mobile_no = request.POST["mobile_no"]
        print "it is a post %s" % starting_point
        print "destination %s" % ending_point
        print "mobile_no %s" % mobile_no

        user_record = {}
        user_record["starting_point"] = starting_point
        user_record["ending_point"] = ending_point
        user_record["mobile_no"] = mobile_no
        kafka_prod_obj.send(mobile_no, json.dumps(user_record))

        return HttpResponse("Thank you for using our App.\
                             You will receive an SMS on traffic alert in case of congestion in %s"%starting_point)

