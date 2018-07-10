import datetime
import json
from time import perf_counter

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, viewsets

from .models import Job
from .serializers import JobSerializer

import logging
my_logger = logging.getLogger(__name__)


class JobViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows jobs to be viewed or created.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


def test_func(request):
    ts = perf_counter()

    my_logger.info('Hello Graylog2. ' + str(datetime.datetime.now().isoformat()), extra={'extra_1': 'ti che???'} )
    my_logger.info('Hello a?.' + str(datetime.datetime.now().isoformat()), extra={'extra_2': 'nu net'}  )
    my_logger.info('Hello b?.' + str(datetime.datetime.now().isoformat()) )

    print('aaa')
    te = perf_counter()
    diff = te - ts
    ms_elapsed = round(diff * 1000, 2)
    my_logger.info('test_func timings', extra={
        'execution_time': ms_elapsed,
    })


    return HttpResponse('шутки шутишь?')

@csrf_exempt
def send_hubspot(request):
    json_data = json.loads(request.body.decode("utf-8"))
    first_name = json_data.get('first_name')
    last_name = json_data.get('last_name')
    email = json_data.get('email')
    phone = json_data.get('phone')
    message_text =  json_data.get('msg')

    rootUrl = 'https://api.hubapi.com/'
    api_key = '5cae4093-3025-4725-8bce-4bcca1d78bd3'
    headers = {'Authorization': 'Bearer ' + api_key}

    resp = requests.get(rootUrl + '/contacts/v1/contact/email/' + email + '/profile?hapikey='+api_key)
    contact_id = None

    json_response = json.loads(resp.text)
    if 'vid' in json_response:
        contact_id = json_response['vid']
    else:
        # create contact
        contact_props = []


        def appendContactKeyValue(name, value):
            contact_props.append({'property': name, "value": value})


        appendContactKeyValue('email', email)
        appendContactKeyValue('firstname', first_name)
        appendContactKeyValue('lastname', last_name)
        appendContactKeyValue('phone', phone)

        resp = requests.post(rootUrl + 'contacts/v1/contact/?hapikey='+api_key, json=dict(properties=contact_props))
        print(resp.content)
        print('=====')
        print('')

        json_response = json.loads(resp.text)
        contact_id = json_response['vid']

    if contact_id is None:
        print('Failed to both get info about email and create user...')

    props = []
    def appendKeyValue(dealname, test_):
        props.append({'name': dealname, "value": test_})

    appendKeyValue('dealname', first_name + ' ' + last_name + ' (from diceus.com)')
    appendKeyValue('dealstage', '204e7085-27ff-426d-9d89-f177996d330e')
    appendKeyValue('pipeline', 'default')
    appendKeyValue('description', message_text)

    associations = dict()
    if contact_id:
        associations = dict(associatedVids=[contact_id])

    resp = requests.post(rootUrl + 'deals/v1/deal?hapikey='+api_key, json=dict(properties=props, associations=associations))


    print(resp.content)
    return  HttpResponse('ufff')


