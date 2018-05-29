from django.http import HttpResponse
from rest_framework import mixins, viewsets

from .models import Job
from .serializers import JobSerializer


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
    import logging
    logger = logging.getLogger('projectname')
    logger.debug('testing message to graylog2')

    import logging
    import graypy

    my_logger = logging.getLogger('test_logger3')
    my_logger.setLevel(logging.DEBUG)

    handler = graypy.GELFHandler('127.0.0.1', 12201)
    my_logger.addHandler(handler)

    my_logger.debug('Hello Graylog2.')

    print('aaa')
    return HttpResponse('aaa')